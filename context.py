from yf_api import *
from strat import *
from exampleSubclass import *

class strat_context:
    def __init__(self, strategy = AllStrategies):
        self.strategy = strategy

    def calculate_BB(self, etf='FNGD'):
        return self.strategy.BandBounce(etf)

    def calculate_MA(self, etf='FNGD'):
        return self.strategy.MovAvg(etf)

