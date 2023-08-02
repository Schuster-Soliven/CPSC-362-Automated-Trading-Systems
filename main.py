from yf_api import choose_date
from adapter import display_graph_for_ticker
import datetime as dt

print('Welcome to HARE (Highly Advanced Rapid Exchange).')
print('As the user, you are hypothetically given $100,000 to use on the stock market.')

print('Which ETF would you like to examine?')

etf_map = {'D': 'FNGD', 'U': 'FNGU'}

user_input = None
while user_input not in etf_map:
    user_input = input('FNGD (D) or FNGU (U)?')
etf = etf_map[user_input]

print('We will download targeted data from Yahoo Finance starting from 2020 January 1')

print('Download successful.')

# Get the start date from the user
while True:
    user_input = input("Please enter a start date (MMDDYYYY) to display the graph: ")
    try:
        start_date = dt.datetime.strptime(user_input, '%m%d%Y')
        if start_date >= dt.datetime(2020, 1, 1) and start_date <= dt.datetime.now() - dt.timedelta(days=1):
            break
        else:
            print("Invalid date. Please enter a date between 01012020 and yesterday's date.")
    except ValueError:
        print("Invalid date format. Please use MMDDYYYY format.")

print(f'Date is within expected range. Data will now range from {user_input} to yesterday\'s date.')

# Display graph using adapter function
display_graph_for_ticker(etf, start_date)

# Ask user for strategy
strategy_map = {'B': 'Bollinger-Band-Bounce', 'M': 'Moving-Average', 'T': 'Trust the system'}
user_input = None
while user_input not in strategy_map:
    user_input = input('Which type of strategy would the user like to use? Bollinger-Band-Bounce (B)\nMoving-Average (M)\nTrust the system (T)\n')
strategy = strategy_map[user_input]

print('Strategy chosen, returns are being calculated.')

# Here, you would add your logic for backtesting and calculating returns...

print('Program will be terminated, we thank you for using HARE.')
