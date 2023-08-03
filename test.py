import unittest
import pandas as pd
from datetime import datetime
from yf_api import choose_date
from strat import *

class Test01_Integration(unittest.TestCase):
    def test_list_int(self):
        ticker = 'FNGU'
        start_date = '01012020'
        y = choose_date(ticker, start_date)
        x = strat.MovAvg(y)
        self.assertEqual(len(x), len(y['Close']))

class Test02_UnitCase(unittest.TestCase):
    def test_list_int(self):
        ticker = 'FNGU'
        start_date = '01011010'
        df = yf_api.choose_date(ticker, start_date)
        self.assertEqual(df, ('Invalid date'))
        print()
        
if __name__ == '__main__':
    with open('test.txt', "w") as f:
        runner = unittest.TextTestRunner(f)
        unittest.main(testRunner=runner)
