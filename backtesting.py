from A_Backtesting import *
from strat import *

class Backtesting(A_Backtesting):
    def __init__(self, strategy, etf_data):
        self.strategy = strategy  # Selected trading strategy
        self.etf_data = etf_data  # Historical ETF data
        self.initial_balance = 100000  # Initial capital for trading
        self.balance = self.initial_balance  # Current available balance
        self.shares = 0  # Number of shares currently owned

    def backtest(self):
        # Determine the strategy's signals
        if self.strategy == 'BandBounce':
            signals = strat.BandBounce(self.etf_data)
        elif self.strategy == 'MovAvg':
            signals = strat.MovAvg(self.etf_data)
        else:
            raise ValueError("Invalid strategy")  # Throw an error if an unsupported strategy is passed

        i = 0
        while i < len(signals):
            signal = signals[i]
            price = self.etf_data['Close'][i]

            # If a sell signal is given but no shares are owned, skip to the next buy signal
            if signal == -1 and self.shares == 0:
                while i < len(signals) and signals[i] != 1:
                    i += 1
                continue

            # Execute buy or sell order at the best price
            if signal == 1:  # Buy at the best price
                self.shares += int(self.balance / price)
                self.balance = 0
            elif signal == -1:  # Sell at the best price
                self.balance += int(self.shares * price)
                self.shares = 0

            i += 1  # Move to the next index after executing the order

        # Sell any remaining shares at the last available price
        final_price = self.etf_data['Close'].iloc[-1]
        final_balance = self.balance + self.shares * final_price
        total_return_dollars = final_balance - self.initial_balance
        total_return_percentage = (total_return_dollars / self.initial_balance) * 100

        return total_return_dollars, total_return_percentage  # Return the final profit or loss
