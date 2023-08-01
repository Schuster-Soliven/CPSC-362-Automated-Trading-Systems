'''
This file: yf_api.py
Description: choose_date returns downloaded data from yahoo finance and get_yesterday gets yesterday's date
'''
import time
from yf_api import *
import pandas as pd
from datetime import datetime, timedelta

def get_yesterday():
    yesterday = datetime.now() - timedelta(days=1)
    yesterday_str = yesterday.strftime("%m%d%Y")
    return yesterday_str

def choose_date(ticker='FNGU', start_date='01012020'):
    print('Grabbing data')
    month = int(start_date[0:2])
    day = int(start_date[2:4])
    year = int(start_date[4:8])
   
    y_str = get_yesterday()

    ymonth = int(y_str[0:2])
    yday = int(y_str[2:4])
    yyear = int(y_str[4:8])

    # start and end dates in Unix time
    period1 = int(time.mktime(datetime(year, month, day, 23, 59).timetuple()))
    period2 = int(time.mktime(datetime(yyear, ymonth, yday, 23, 59).timetuple()))
    interval = '1d' 

    # API endpoint
    url = f'https://query1.finance.yahoo.com/v7/finance/download/{ticker}?period1={period1}&period2={period2}&interval={interval}&events=history&includeAdjustedClose=true'

    # Get data
    df = pd.read_csv(url)

    # Save dataframe to JSON file
    df.to_json(f"{ticker}.json", orient="records", date_format="iso")

    return df

