import unittest
import pandas as pd
from yf_api import choose_date
from strat import BandBounce

class TestIntegration(unittest.TestCase):
    def test_integration(self):
        # Step 1: Call the Yahoo Finance API and get the data
        data = choose_date('FNGU', '01012020')
        data = data[['Date', 'Close']]

        # Step 2: Implement the Bollinger Band Bounce trading strategy
        result = BandBounce(data)

        
        expected_result = [-1, 0, 1, 1, -1, 0, 0, 1, -1, 0]

        self.assertEqual(result, expected_result)

if __name__ == '__main__':
    unittest.main()
