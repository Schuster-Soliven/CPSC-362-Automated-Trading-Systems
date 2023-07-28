from yf_api import *
from displayGraph import plot_data
import datetime

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
if (user_input == 'D'):
    df = choose_date('FNGD', '01012020')
else:
    df = choose_date('FNGU', '01012020')

print('Download successful.')

# Ask user for start date
# user_input = None
# while (not isinstance(user_input, int) or user_input <= 1012020):
#     user_input = int(input('Please enter a start date (MMDDYYYY) of which will contain ETF information until the end date of (yesterday). Note that the maximum range is 01012020: '))
# print(f'Date is within expected range. Data will now range from {user_input} to yesterday\'s date.')

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

# Ask user for strategy
strategy_map = {'B': 'Bollinger-Band-Bounce', 'M': 'Moving-Average', 'T': 'Trust the system'}
user_input = None
while user_input not in strategy_map:
    user_input = input('Which type of strategy would the user like to use? Bollinger-Band-Bounce (B)\nMoving-Average (M)\nTrust the system (T)\n')
strategy = strategy_map[user_input]

print('Strategy chosen, returns are being calculated.')

# Here, you would add your logic for backtesting and calculating returns...

print('Program will be terminated, we thank you for using HARE.')
