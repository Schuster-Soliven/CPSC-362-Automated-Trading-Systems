import time
import pandas as pd
from datetime import datetime, timedelta

def choose_date(etf='FNGU', start_date='01012020'):
    month = int(start_date[0:2])
    day = int(start_date[2:4])
    year = int(start_date[4:8])

    yesterday = datetime.now() - timedelta(days=1)
    yesterday_str = yesterday.strftime("%m%d%Y")

    ymonth = int(yesterday_str[0:2])
    yday = int(yesterday_str[2:4])
    yyear = int(yesterday_str[4:8])

    # start and end dates in Unix time
    period1 = int(time.mktime(datetime(year, month, day, 23, 59).timetuple()))
    period2 = int(time.mktime(datetime(yyear, ymonth, yday, 23, 59).timetuple()))
    interval = '1d' 

    # API endpoint
    url = f'https://query1.finance.yahoo.com/v7/finance/download/{etf}?period1={period1}&period2={period2}&interval={interval}&events=history&includeAdjustedClose=true'

    # Get data
    df = pd.read_csv(url)

    # Save dataframe to JSON file
    df.to_json(f"{etf}.json", orient="records", date_format="iso")

    return df
