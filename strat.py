#module contains both Bollinger Band Bounce and Moving Average Crossover
from yf_api import *

def BandBounce(file):
    print('standard dev')
    # TO DO
    # pull 'close' data
    # calculate middle, upper, and lower bands
    #ASSUMING THAT    window = 20    band (std dev) = 2
    #when upper & lower bands squeeze together, good sign to buy/sell cuz will usually expand after
    mean = file.rolling(window=20).mean()
    stdDev = file.rolling(window=20).mean()
    uBand = mean + 2 * stdDev
    lBand = mean - 2 * stdDev

    #call backtest

def MovAvg(file):
    print('average')


def BandBounceTest():
    #maybe