'''
This file: main.py
Description: User interface
'''
from strat import *
from graph_api_adapter import TickerGraphDisplayer
import os

def remove_file(filename):
    if os.path.exists(filename):
        os.remove(filename)

remove_file('FNGD.json')
remove_file('FNGU.json')

print('Welcome to HARE (Highly Advanced Rapid Exchange).')
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
y = choose_date(etf, start_date)
# Create an instance of TickerGraphDisplayer
graph_displayer = TickerGraphDisplayer(start_date)

print(f'Date is within expected range. Data will now range from {start_date} to yesterday\'s date.')


# Ask user for strategy
strategy_map = {'B': 'Bollinger-Band-Bounce', 'M': 'Moving-Average', 'T': 'Trust the system'}
user_input = None
while user_input not in strategy_map:
    user_input = input('Which type of strategy would the user like to use? Bollinger-Band-Bounce (B)\nMoving-Average (M)\nTrust the system (T)\n')
if user_input == 'B' or user_input == 'Bollinger-Band-Bounce':
    d = give_date(y, BandBounce(y))
    for x in d.items():
        print(x)
elif user_input == 'M' or user_input == 'Moving-Average':
    d = give_date(y, MovAvg(y))
    for x in d.items():
        print(x)
else:
    print('Trust the System WIP')

print('Strategy chosen, returns are being calculated.')

# Here, you would add your logic for backtesting and calculating returns...

# Display graph for the selected ETF
graph_displayer.display_graph_for_ticker(etf)

print('Program will be terminated, we thank you for using HARE.')
