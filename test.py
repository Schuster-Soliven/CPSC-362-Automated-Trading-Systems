import unittest
import io
import sys
from unittest.mock import patch
import json

from yf_api import *

dataFile = 'FNGD.json'


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
        #self.assertEqual(list, type(data))
        remove_file(dataFile)

if __name__ == '__main__':
    with open('test.txt', "w") as f:
        runner = unittest.TextTestRunner(f)
        unittest.main(testRunner=runner)
        