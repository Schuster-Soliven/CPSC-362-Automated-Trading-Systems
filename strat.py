#module contains both Bollinger Band Bounce and Moving Average Crossover
from yf_api import *


def BandBounce(file, window=20):
    #pull 'close' data
    file = file['Close']

    #calculate middle, upper, and lower bands
    #ASSUMING THAT    window = 20    band (std dev) = 2
    #when upper & lower bands squeeze together, good sign to buy/sell cuz will usually expand after
    mean = file.rolling(window).mean()
    stdDev = file.rolling(window).std()
    uBand = mean + 2 * stdDev
    lBand = mean - 2 * stdDev
    
    #create list of calls to buy / sell / do nothing
    callist = []
    for n in range(len(file)):
        #print(file[n])
        if file[n] > uBand[n]:     #buy (-1)
            callist.append(-1)
        elif file[n] < lBand[n]:   #sell (1)
            callist.append(1)
        else:                   #do nothing (0)
            callist.append(0)

    #call backtesting module
    #print(callist)




#def MovAvg(file):
    #print('average')


#def BandBounceTest():
    #maybe


BandBounce(choose_date())
