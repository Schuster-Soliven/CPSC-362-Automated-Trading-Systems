import unittest
import pandas as pd
from strat import BandBounce

class TestBandBounce(unittest.TestCase):
    def test_BandBounce(self):
        data = pd.read_json('FNGU.json')  # replace with your JSON file
        data = data[['Date', 'Close']]  # assuming the file only contains 'Date' and 'Close' columns
        result = BandBounce(data)
        
        
        expected_result = [-1, 0, 1, 1, -1, 0, 0, 1, -1, 0]
        
        self.assertEqual(result, expected_result)

if __name__ == '__main__':
    unittest.main()
