from yf_api import *

print('Welcome to HARE (Highly Advanced Rapid Exchange).')
print('As the user, you are hypothetically given $100,000 to use on the stock market.')

print('Which ETF would you like to examine?')

etf_map = {'D': 'FNGD', 'U': 'FNGU'}

user_input = None
while user_input not in etf_map:
    user_input = input('FNGD (D) or FNGU (U)?')
etf = etf_map[user_input]

print('We will download targeted data from Yahoo Finance starting from 2020 January 1')

# Download data!
start_date = '01012020'
choose_date(etf, start_date)
print('Download successful.')

# Ask user for start date
user_input = None
while (not isinstance(user_input, int) or user_input <= 1012020):
    user_input = int(input('Please enter a start date (MMDDYYYY) of which will contain ETF information until the end date of (yesterday). Note that the maximum range is 01012020: '))
print(f'Date is within expected range. Data will now range from {user_input} to yesterday\'s date.')

# Ask user for strategy
strategy_map = {'B': 'Bollinger-Band-Bounce', 'M': 'Moving-Average', 'T': 'Trust the system'}
user_input = None
while user_input not in strategy_map:
    user_input = input('Which type of strategy would the user like to use? Bollinger-Band-Bounce (B)\nMoving-Average (M)\nTrust the system (T)\n')
strategy = strategy_map[user_input]

print('Strategy chosen, returns are being calculated.')

# Here, you would add your logic for backtesting and calculating returns...

print('Program will be terminated, we thank you for using HARE.')
