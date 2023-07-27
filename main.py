from yf_api import *
from displayGraph import plot_data
import datetime

# Introduction Prompt
print('Welcome to HARE (Highly Advanced Rapid Exchange).')
print('As the user, you are hypothetically given $100,000 to use on the stock market.')

# Start of loop
# ETF choice
print('Which ETF would you like to examine?')

user_input = 'NULL'
while (user_input != 'U' and user_input != 'D') :
    etf = input('FNGD (D) or FNGU (U)?')
    user_input = etf.upper()

print('We will download targeted data from Yahoo Finance starting from 2020 January 1')

# # Download data!
# if (user_input == 'D'):
#     df = choose_date('FNGD')
# else:
#     df = choose_date()

# print('Download successful.')

# Download data!
if (user_input == 'D'):
    df = choose_date('FNGD', '01012020')
else:
    df = choose_date('FNGU', '01012020')

print('Download successful.')

# Convert 'Date' column to datetime objects
df['Date'] = pd.to_datetime(df['Date'])

# Get the start date from the user
while True:
    user_input = input("Please enter a start date (MMDDYYYY) to display the graph: ")
    try:
        start_date = datetime.datetime.strptime(user_input, '%m%d%Y')
        if start_date >= datetime.datetime(2020, 1, 1) and start_date <= datetime.datetime.now() - datetime.timedelta(days=1):
            break
        else:
            print("Invalid date. Please enter a date between 01012020 and yesterday's date.")
    except ValueError:
        print("Invalid date format. Please use MMDDYYYY format.")

print(f'Date is within expected range. Data will now range from {user_input} to yesterday\'s date.')

# Filter DataFrame based on the user's input date
df = df[df['Date'] >= start_date]

# Display graph
plot_data(df, user_input)


# User prompt to choose strategy
while True:
    print('Which type of strategy would you like to use?')
    user_input = input('Bollinger-Band-Bounce (B)\nMoving-Average (M)\nTrust the system (T)\n')
    user_input = user_input.upper()
    if user_input in ['B', 'M', 'T']:
        break
    else:
        print("Invalid input. Please choose one of the provided options.")

print('Strategy chosen, returns are being calculated.')


# backtest
# returns are calculated
# user another strategy?
# try program again?

# End Program
print('Program will be terminated. Thank you for using HARE.')
