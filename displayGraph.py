import pandas as pd
from yf_api import *
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

def plot_data(df):
    """
    Plots the data for the chosen ETF.

    Parameters:
        df (pandas.DataFrame): DataFrame containing the historical financial data.
        ticker (str): The ticker symbol of the ETF.

    Returns:
        None
    """
    # Convert 'Date' column to datetime objects
    df['Date'] = pd.to_datetime(df['Date'])

    plt.figure(figsize=(12, 6))
    plt.plot(df['Date'], df['Close'], label='Close Price', color='red')
    plt.xlabel('Date')
    plt.ylabel('Closing Price')

    # Format the date with hyphens
    formatted_date = df['Date'].iloc[0].strftime('%m-%d-%Y')
    formatted_date2 = df['Date'].iloc[-1].strftime('%m-%d-%Y')
    plt.title(f'Historical Closing Price from {formatted_date} to {formatted_date2}')

    plt.legend()
    plt.grid(True)

    # Set the x-axis tick locator and formatter
    ax = plt.gca()
    ax.xaxis.set_major_locator(mdates.AutoDateLocator())
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%m-%d-%Y'))
    plt.xticks(rotation=45)

    # Display graph
    plt.tight_layout()
    plt.show()
    return 0

