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

    def __init__(self, strat_ = strat, start_date_ = '01012020'):
        self.start_date_ = start_date_
        self.strat_ = strat_

    def get_start_date(self):
        return self.start_date_
        
    def get_strat_(self):
        return self.strat_
    
    def display_graph_for_ticker(self, etf_data):
        # This method takes a ticker symbol and uses it to fetch data for the given date, '01012020', using the choose_date function

        # Call the plot_data method of the DisplayGraph instance to plot the graph
        dG = DisplayGraph(etf_data, self.start_date_)
        dG.add_line('Close', etf_data['Close'])
        dG.plot_data()
        return 0
    
    
    def display_band_bounce(self, etf_data):
        bb_graph = DisplayGraph(etf_data, self.start_date_)
        self.strat_.BandBounce(etf_data)
        ub = self.strat_.getuBands()
        lb = self.strat_.getlBands()
        bb_graph.add_line('Close', etf_data['Close'])
        bb_graph.add_line('uBound', ub)
        bb_graph.add_line('lBound', lb)
        bb_graph.plot_data()

    def display_moving_average(self, etf_data):
        ma_graph = DisplayGraph(etf_data, self.start_date_)
        self.strat_.MovAvg(etf_data)
        avg = self.strat_.getAvg()
        ma_graph.add_line('Close', etf_data['Close'])
        ma_graph.add_line('Moving Avg', avg)
        ma_graph.plot_data()
        