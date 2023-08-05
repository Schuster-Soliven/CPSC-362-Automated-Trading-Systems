'''
DisplayGraph class that displays a graph using Close Price vs Date
'''
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from A_display_graph import *
from yf_api import *

class DisplayGraph(A_display_graph):
    def __init__(self, df, start_date):
        self.df = df
        # Convert 'Date' column to datetime objects and filter by start_date
        self.df['Date'] = pd.to_datetime(df['Date'])
        self.df = self.df[self.df['Date'] >= pd.to_datetime(start_date, format="%m%d%Y")]
        self.lst = []

    def add_line(self, name, data):
        '''Adds a Dictionary of desired data to be plotted based on the name and list of data'''
        self.lst.append({name : data})

    def plot_data(self):
        '''Plots the data points onto the graph depending on contents of lst'''
        oG = plt
        oG.figure(figsize=(12, 6))
        # Plot the 'Close' column against the 'Date' column
        for x in self.lst:
            for key, value in x.items():
                if key == 'Close':
                    oG.plot(self.df['Date'], value, label='Close Price', color='red')
                elif key == 'uBound':
                    oG.plot(self.df['Date'], value, label='Upper Bound', color='blue')
                elif key == 'lBound':
                    oG.plot(self.df['Date'], value, label='Lower Bound', color='yellow')
                elif key == 'Moving Avg':
                    oG.plot(self.df['Date'], value, label='Moving Average', color='orange')
                else:
                    break
        
        # Label the x-axis
        oG.xlabel('Date')
        # Label the y-axis
        oG.ylabel('Closing Price')

        # Format the start and end dates to create a title for the graph
        formatted_date = self.df['Date'].iloc[0].strftime('%m-%d-%Y')
        formatted_date2 = self.df['Date'].iloc[-1].strftime('%m-%d-%Y')
        oG.title(f'Historical Closing Price from {formatted_date} to {formatted_date2}')

        # Add a legend to the graph
        oG.legend()
        # Add grid lines to the graph
        oG.grid(True)

        # Set the x-axis tick locator and formatter to control date display
        ax = plt.gca()
        ax.xaxis.set_major_locator(mdates.AutoDateLocator())
        ax.xaxis.set_major_formatter(mdates.DateFormatter('%m-%d-%Y'))
        # Rotate the x-axis labels for better visibility
        oG.xticks(rotation=45)

        # Ensure that the layout fits well
        oG.tight_layout()
        # Display the graph
        oG.show()
        return 0
