import unittest
import pandas as pd
from datetime import datetime
from yf_api import choose_date
from strat import *

class TestyfAPI(unittest.TestCase):
    def test_list_int(self):
        ticker = 'FNGU'
        start_date = '01012020'
        y = choose_date(ticker, start_date)
        x = MovAvg(y)
        self.assertEqual(len(x), len(y['Close']))

class TestIntegration(unittest.TestCase):
    def test_list_int(self):
        ticker = 'FNGU'
        start_date = '01011010'
        df = choose_date(ticker, start_date)
        self.assertEqual(df, ('Invalid date'))
        print()
        
if __name__ == '__main__':
    with open('test.txt', "w") as f:
        runner = unittest.TextTestRunner(f)
        unittest.main(testRunner=runner)