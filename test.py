from yf_api import *
from strat import *
from exampleSubclass import *
from allStrategies import *
from context import *

import unittest
import pandas as pd
from datetime import datetime

class Test01_Integration(unittest.TestCase):
    def test_list_int(self):
        ticker = 'FNGU'
        start_date = '01012020'
        y = yf_api.choose_date(ticker, start_date)
        x = strat.MovAvg(y)
        self.assertEqual(len(x), len(y['Close']))

class Test02_UnitCase(unittest.TestCase):
    def test_list_int(self):
        ticker = 'FNGU'
        start_date = '01011010'
        df = yf_api.choose_date(ticker, start_date)
        self.assertEqual(df, ('Invalid date'))
        print()

class Test03_StrategyPatternBandBounceActual(unittest.TestCase):
    def test_list_int(self):
        x = strat
        m = strat_context(x)
        
        k = m.calculate_BB(yf_api.choose_date())
        self.assertEqual(list, strat.BandBounce(k))
        print()

class Test04_StrategyPatternMovingAverageFake(unittest.TestCase):
    def test_list_int(self):  
        y = exampleSubclass
        n = strat_context(y)
        j =  n.calculate_MA('FNGD')
        self.assertEqual(str,type(j))
        print()
        
if __name__ == '__main__':
    with open('test.txt', "w") as f:
        runner = unittest.TextTestRunner(f)
        unittest.main(testRunner=runner)
