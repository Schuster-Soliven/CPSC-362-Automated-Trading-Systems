
import time
import datetime
import pandas as pd

# choose FNGD or FNGU
ticker = 'FNGU'
# user input
period1 = int(time.mktime(datetime.datetime(2020, 12, 1, 23, 59).timetuple()))
# yesterday's date
period2 = int(time.mktime(datetime.datetime(2020, 12, 31, 23, 59).timetuple()))
interval = '1d' # 1d, 1m

API_endpoint = f'https://query1.finance.yahoo.com/v7/finance/download/{ticker}?period1={period1}&period2={period2}&interval={interval}&events=history&includeAdjustedClose=true'

df = pd.read_csv(API_endpoint)
print(df)
print(df.to_json())
