import yfinance as yf
from datetime import datetime, timedelta

# Get yesterday's date
yesterday = datetime.now() - timedelta(days=1)
yesterday_str = yesterday.strftime("%Y-%m-%d")


# Define a function to download and save data
def download_and_save(ticker, start, end):
    # this line downloads data
    data = yf.download(ticker, start=start, end=end)
    data = data[["Open", "High", "Low", "Close", "Volume"]]  # select necessary columns
    data.reset_index(inplace=True)  # to include date in the json file
    data.to_json(f"{ticker}_data.json", orient="records", date_format="iso")

download_and_save("FNGU", start="2020-01-01", end=yesterday_str)