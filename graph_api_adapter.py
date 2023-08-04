# Import the choose_date function from yf_api module
from yf_api import *
from strat import *

# Import the DisplayGraph class from displayGraph module
from displayGraph import DisplayGraph

# Define a class named TickerGraphDisplayer to display graphs for tickers
class TickerGraphDisplayer(DisplayGraph):
    #def __init__(self, start_date):
        # Constructor takes start_date as an argument and initializes the instance variable
        #self.start_date = start_date

    def __init__(self, strat_ = strat):
        self.strat_ = strat_


    def display_graph_for_ticker(self, ticker):
        # This method takes a ticker symbol and uses it to fetch data for the given date, '01012020', using the choose_date function
        df = yf_api.choose_date(ticker, '01012020')

        # Check if the returned value is a string (an error message) and print it if so
        if isinstance(df, str):
            print(df)
            return

        # Create an instance of the DisplayGraph class with the obtained data frame (df) and the start date
        graph = DisplayGraph(df, self.start_date)


        # Call the plot_data method of the DisplayGraph instance to plot the graph
        graph.plot_data()
    
    
    def display_band_bounce(self, ticker):
        df = yf_api.choose_date(ticker, '01012020')
        graph = DisplayGraph(df, self.start_date)
        up = DisplayGraph(strat.getuBand(), '01012020')
        low = DisplayGraph(strat.getlBand(), '01012020')
        graph.plot_data()
