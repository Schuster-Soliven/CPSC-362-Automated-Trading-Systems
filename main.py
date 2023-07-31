from yf_api import *
from strat import *

print('Welcome to HARE (Highly Advanced Rapid Exchange).')
print('As the user, you are hypothetically given $100,000 to use on the stock market.')

print('Which ETF would you like to examine?')

etf_map = {'D': 'FNGD', 'U': 'FNGU'}

user_input = None
while user_input not in etf_map:
    user_input = input('FNGD (D) or FNGU (U)?')
etf = etf_map[user_input]

'''
# Probably unnecessary
print('We will download targeted data from Yahoo Finance starting from 2020 January 1')
print('Download successful.')
'''

# Ask user for start date
user_input = '00000000'
while (int(user_input[0:2]) > 12 or int(user_input[2:4]) > 31 or int(user_input[4:8]) < 2020):
    user_input = input('Please enter a start date (MMDDYYYY) of which will contain ETF information until the end date of (yesterday). Note that the maximum range is 01012020: ')
start_date = user_input
y = choose_date(etf, start_date)
print(f'Date is within expected range. Data will now range from {start_date} to yesterday\'s date.')

# add graph here
print(f'Displaying a graph and tabulated data ranging from {start_date} to {get_yesterday()}')

# Ask user for strategy
strategy_map = {'B': 'Bollinger-Band-Bounce', 'M': 'Moving-Average', 'T': 'Trust the system'}

user_input = None
while user_input not in strategy_map:
    user_input = input('Which type of strategy would the user like to use? Bollinger-Band-Bounce (B)\nMoving-Average (M)\nTrust the system (T)\n')
if user_input == 'B' or user_input == 'Bollinger-Band-Bounce':
    print(BandBounce(y))
else:
    print(MovAvg(y))

print('Strategy chosen, returns are being calculated.')

# Here, you would add your logic for backtesting and calculating returns...

print('Program will be terminated, we thank you for using HARE.')
