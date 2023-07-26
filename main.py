#dfrom download_data import *
from yf_api import *

# Introduction Prompt
print('Welcome to HARE (Highly Advanced Rapid Exchange).')
print('As the user, you are hypothetically given $100,000 to use on the stock market.')

# Start of loop
# ETF choice
print('Which ETF would you like to examine?')

user_input = 'NULL'
while (user_input != 'U' and user_input != 'D') :
    user_input = input('FNGD (D) or FNGU (U)?')

print('We will download targeted data from Yahoo Finance starting from 2020 January 1')

# Download data!
date = 'NULL'
if (date == 'D') : 
    # download_and_save("FNGD", start="2020-01-01", end=yesterday_str)
    choose_date('FNGD')
else:
   choose_date()
print('Download successful.')


# Select Range
while((int != type(user_input) or user_input <= int("01012020"))):
    # change if to be acceptable
    user_input = input('Please enter a start date (MMDDYYYY) of which will contain ETF information until the end date of (yesterday). Note that the maximum range is 01012020: ')
print('Date is within expected range. Data will now range from ' + user_input + ' to yesterday\'s date.')

# User prompt to choose strategy
print('The user is automatically given to have $100,000 before strategy simulation.')
while(user_input != 'B' or user_input != 'M' or user_input != 'T'):
    print('Which type of strategy would the user like to use?')
    user_input = input('Bollinger-Band-Bounce (B)\nMoving-Average (M)\nTrust the system (T)\n')
print('Strategy chosen, returns are being calculated.')

# backtest
# returns are calculated
# user another strategy?
# try program again?

# End Program
print('Program will be terminated, we thank you for using HARE.')