import time
import datetime
import pandas as pd
from datetime import datetime, timedelta



# choose date based on user inputed etf
def choose_date(str1='FNGU', str2='01012020'):
    ticker = str1
    month = int(str2[0:2])
    day = int(str2[2:4])
    year = int(str2[4:8])
    
    yesterday = datetime.now() - timedelta(days=1)
    yesterday_str = yesterday.strftime("%m%d%Y")
    print()

    ymonth = int(yesterday_str[0:2])
    yday = int(yesterday_str[2:4])
    yyear = int(yesterday_str[4:8])
    # start date
    period1 = int(time.mktime(datetime(year, month, day, 23, 59).timetuple()))
    # yesterday's date
    period2 = int(time.mktime(datetime(yyear, ymonth, yday, 23, 59).timetuple()))
    interval = '1d' 
    # grabs data
    API_endpoint = f'https://query1.finance.yahoo.com/v7/finance/download/{ticker}?period1={period1}&period2={period2}&interval={interval}&events=history&includeAdjustedClose=true'
    df = pd.read_csv(API_endpoint)
    # print me
    print(df)
    # json file dictionary wrong
    
    #df.reset_index(inplace=True)
    print(df)
    # what is f and what is r
    df.to_json(f"{ticker}.json", orient="records", date_format="iso")
    print(df)
    # creates a file
    file1 = open(str1+'.json', 'w')
    # why do I need to put to json again
    file1.write(df.to_json())
    file1.close()
    return df

'''
random = choose_date('FNGD', '03252021') # month day year
print(random)
print(random.to_json())
'''

choose_date()