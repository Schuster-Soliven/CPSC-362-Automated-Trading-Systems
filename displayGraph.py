import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

class DisplayGraph:
    def __init__(self, df, start_date):
        self.df = df
        # Convert 'Date' column to datetime objects and filter by start_date
        self.df['Date'] = pd.to_datetime(df['Date'])
        self.df = self.df[self.df['Date'] >= pd.to_datetime(start_date, format="%m%d%Y")]


    def plot_data(self):
        # Create a new figure with specific size
        plt.figure(figsize=(12, 6))
        # Plot the 'Close' column against the 'Date' column
        plt.plot(self.df['Date'], self.df['Close'], label='Close Price', color='red')
        # Label the x-axis
        plt.xlabel('Date')
        # Label the y-axis
        plt.ylabel('Closing Price')

        # Format the start and end dates to create a title for the graph
        formatted_date = self.df['Date'].iloc[0].strftime('%m-%d-%Y')
        formatted_date2 = self.df['Date'].iloc[-1].strftime('%m-%d-%Y')
        plt.title(f'Historical Closing Price from {formatted_date} to {formatted_date2}')

        # Add a legend to the graph
        plt.legend()
        # Add grid lines to the graph
        plt.grid(True)

        # Set the x-axis tick locator and formatter to control date display
        ax = plt.gca()
        ax.xaxis.set_major_locator(mdates.AutoDateLocator())
        ax.xaxis.set_major_formatter(mdates.DateFormatter('%m-%d-%Y'))
        # Rotate the x-axis labels for better visibility
        plt.xticks(rotation=45)

        # Ensure that the layout fits well
        plt.tight_layout()
        # Display the graph
        plt.show()
        return 0