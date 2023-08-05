'''
A subclass of AllStrategies for the purpose of demonstrating the Strategy pattern
'''
from allStrategies import *

class exampleSubclass(AllStrategies):
    def BandBounce(etf_data):
        return("I am bouncing a band")
    def MovAvg(etf_data):
        return("I am moving across an average")
