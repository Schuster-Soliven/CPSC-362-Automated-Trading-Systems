'''
This file: main.py
Description: User interface
'''
from yf_api import *
from strat import *
from displayGraph import *
from backtesting import *
from graph_api_adapter import *
import os

def remove_file(filename):
    if os.path.exists(filename):
        os.remove(filename)

print('Welcome to HARE (Highly Advanced Rapid Exchange).')
y_instance = yf_api
key = 'Y'
while(key == 'Y'):
    print('As the user, you are hypothetically given $100,000 to use on the stock market.')
    print('Which ETF would you like to examine?')

    etf_map = {'D': 'FNGD', 'U': 'FNGU'}

    user_input = None
    while user_input not in etf_map:
        user_input = input('FNGD (D) or FNGU (U)?')
    etf = etf_map[user_input]

    # Ask user for start date
    user_input = '00000000'
    while (int(user_input[0:2]) > 12 or int(user_input[2:4]) > 31 or int(user_input[4:8]) < 2020):
        user_input = input('Please enter a start date (MMDDYYYY) of which will contain ETF information until the end date of (yesterday). Note that the maximum range is 01012020: ')
    start_date = user_input
    y = y_instance.choose_date(etf, start_date)
    graph_displayer = TickerGraphDisplayer(start_date)

    print(f'Date is within expected range. Data will now range from {start_date} to yesterday\'s date.')

    # add graph here
    print(f'Displaying a graph and tabulated data ranging from {start_date} to {get_yesterday()}')
    graph_displayer.display_graph_for_ticker(y)

    # Ask user for strategy
    strategy_map = {'B': 'Bollinger-Band-Bounce', 'M': 'Moving-Average'}
    user_input = None
    prompt = 'Y'
    total_return_dollars = ''
    total_return_percentage = ''
    ll = strat()
    while(prompt == 'Y'):
        while user_input not in strategy_map:
            user_input = input('Which type of strategy would the user like to use? Bollinger-Band-Bounce (B)\nMoving-Average (M)\n')
        if user_input == 'B' or user_input == 'Bollinger-Band-Bounce':
            bb = ll.BandBounce(y)
            d = give_date(y, ll.BandBounce(y))
            bb_graph = TickerGraphDisplayer(ll, start_date)
            bb_graph.display_band_bounce(y)
            for x in d.items():
                print(x)
                # Initialize and backtest the BandBounce strategy
            band_bounce_backtesting = Backtesting('BandBounce')
            total_return_dollars, total_return_percentage = band_bounce_backtesting.backtest(y, bb)
            print('Strategy chosen, returns are being calculated.')
            print("BandBounce Strategy Results: ")
        elif user_input == 'M' or user_input == 'Moving-Average':
            ma = ll.MovAvg(y)
            d = give_date(y, ll.MovAvg(y))
            ma_graph = TickerGraphDisplayer(ll, start_date)
            ma_graph.display_moving_average(y)
            for x in d.items():
                print(x)
                    # Initialize and backtest the MovAvg strategy
            mov_avg_backtesting = Backtesting('MovAvg')
            total_return_dollars, total_return_percentage = mov_avg_backtesting.backtest(y, ma)
            print('Strategy chosen, returns are being calculated.')
            print("Moving Average Strategy Results: ")
        else:
            print('Choose another Strategy')

        print("Total Return in Dollars:  $", total_return_dollars)
        print("Total Return in Percentage:", total_return_percentage, "%")
        prompt = input('Would you like to try using a different strategy? Y/N ')
        user_input = ''

    key = input('Would you like to continue using HARE? Y/N ')
    
print('Program will be terminated, we thank you for using HARE.')

remove_file('FNGD.json')
remove_file('FNGU.json')
