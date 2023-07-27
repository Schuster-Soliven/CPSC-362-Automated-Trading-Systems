import unittest
import io
import sys
from unittest.mock import patch
import json

from download_data import *

dataFile = 'FNGD_data.json'


import os
def remove_file(filename):
    if os.path.exists(filename):
        os.remove(filename)

# Fix me to work with yf_api
class Test01_FileContentsIsList(unittest.TestCase):
    def test_list_int(self):
        """
        *** Test01 *** JSON file with ETF data exists for FNGD***
        """
        download_and_save("FNGD", start="2020-01-01", end=yesterday_str)
        try:
            with open(dataFile) as f:
                # call download function and dump into f
                data = json.load(f)
                # load dataFile contents into data
                self.assertEqual(list, type(data))
                # making sure data is type list
        except FileNotFoundError:
            print("FAIL: File not found")

        except json.JSONDecodeError:
            print("FAIL: Unable to parse JSON")
            
        remove_file(dataFile)

'''   
class Test02_AccurateDayCount(unittest.TestCase):
    def test_list_int(self):
        """
        *** Test02 *** Opens JSON File and counts items in list ***
        """
        #data should be a list of dictionaries
        download_and_save("FNGD", start="2020-01-01", end=yesterday_str)
        with open(dataFile) as f:
            data = json.load(f)
            if (len(data) >= 890):
                key = True
            self.assertEqual(key, True)
        remove_file(dataFile)

class Test03_MatchDay(unittest.TestCase):
    def test_list_int(self):
        """
        *** Test03 *** Data is consistent with a given day ***
        """
        #data should be a list of dictionaries
        with open(dataFile) as f:
            data = json.load(f)
        self.assertEqual(data[0], {"Date":"2020-01-02T00:00:00.000","Open":62.1199989319,"High":65.2099990845,"Low":62.0800018311,"Close":65.2099990845,"Volume":155900})
        '''    
'''
class Test05_GraphExists(unittest.TestCase):
    def test_list_int(self):
        print('')
'''
if __name__ == '__main__':
    with open('test.txt', "w") as f:
        runner = unittest.TextTestRunner(f)
        unittest.main(testRunner=runner)
        
        
    # This is a data point for one day (List of dictionaries)
    # {"Date":"2020-01-02T00:00:00.000","Open":62.1199989319,"High":65.2099990845,"Low":62.0800018311,"Close":65.2099990845,"Volume":155900} 