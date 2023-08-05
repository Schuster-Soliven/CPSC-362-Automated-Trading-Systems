'''
An adaptor class between displayGraph and strat that allows data to be taken from strat to be plotted in displayGraph
'''
from yf_api import *
from strat import *
from displayGraph import DisplayGraph

# Define a class named TickerGraphDisplayer to display graphs for tickers
class TickerGraphDisplayer(DisplayGraph):
    def __init__(self, strat_ = strat, start_date_ = '01012020'):
        self.start_date_ = start_date_
        self.strat_ = strat_

    def get_start_date(self):
        '''return start date'''
        return self.start_date_
        
    def get_strat_(self):
        '''return strat object'''
        return self.strat_
    
    def display_graph_for_ticker(self, etf_data):
        '''
        Takes in etf close price data to call displayGraph's plot_data
        '''

        # Call the plot_data method of the DisplayGraph instance to plot the graph
        dG = DisplayGraph(etf_data, self.start_date_)
        dG.add_line('Close', etf_data['Close'])
        dG.plot_data()
        return 0
    
    
    def display_band_bounce(self, etf_data):
        '''
        Takes upper and lower bounds of strat after a BandBoudn has been called to DisplayGraph via add_line to plot upper, lower, and Close price data onto a graph
        '''
        bb_graph = DisplayGraph(etf_data, self.start_date_)
        self.strat_.BandBounce(etf_data)
        ub = self.strat_.getuBands()
        lb = self.strat_.getlBands()
        bb_graph.add_line('Close', etf_data['Close'])
        bb_graph.add_line('uBound', ub)
        bb_graph.add_line('lBound', lb)
        bb_graph.plot_data()

    def display_moving_average(self, etf_data):
        '''
        Takes the moving average data of strat after movavg has been called to DisplayGraph via add_line to plot Moving Average and Close price data onto a graph
        '''
        ma_graph = DisplayGraph(etf_data, self.start_date_)
        self.strat_.MovAvg(etf_data)
        avg = self.strat_.getAvg()
        ma_graph.add_line('Close', etf_data['Close'])
        ma_graph.add_line('Moving Avg', avg)
        ma_graph.plot_data()
        
