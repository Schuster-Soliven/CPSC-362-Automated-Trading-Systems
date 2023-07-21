from download_data import *

# Introduction Prompt
print('Welcome to HARE (Highly Advanced Rapid Exchange).')
print('As the user, you are hypothetically given $100,000 to use on the stock market.')

# ETF choice
print('Which ETF would you like to examine?')

user_input = 'NULL'
while (user_input != 'U' or user_input != 'D') :
    print('FNGD (D) or FNGU (U)?')
    user_input = input('FNGD (D) or FNGU (U)?')

print('We will download targeted data from Yahoo Finance starting from 2020 January 1')

if (user_input == 'D') : 
    download_and_save("FNGD", start="2020-01-01", end=yesterday_str)
else:
    download_and_save("FNGU", start="2020-01-01", end=yesterday_str)

    