from yf_api import *
from strat import *
from exampleSubclass import *

class strat_context:
    def __init__(self, strategy = AllStrategies):
        self.strategy = strategy

    def calculate_BB(self, etf):
        return self.strategy.BandBounce(etf)

    def calculate_MA(self, etf):
        return self.strategy.MovAvg(etf)

a = yf_api   
b = a.choose_date()
x = strat
y = exampleSubclass
m = strat_context(x)
n = strat_context(y)

print(m.calculate_BB(b))

print(n.calculate_BB(b))
