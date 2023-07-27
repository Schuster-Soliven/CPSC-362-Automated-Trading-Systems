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

# use 20 days as data points
def MovAvg(ticker):
    # iter over dictionary taking close data
    # check previous data point and next data point. If next data point is under or below the average, buy or sell
    
    #should print all close indices
    for x in ticker['Close']:
        print(x)

    counter = 20
    i = 0
    sum = 0
    average = 0
    while(i < 20):
        average_list[i] = ticker['Close'][i]
        
    average_list = []
    for x in ticker['Close']:
        if(i < 20):
            i+=1
            average_list.append(x)
        else:
            break
    i = 0
 
    # should iterate starting from 0, and summate 20 indices and calculate avg 
    while(i < len(ticker['Close'])):
        if (counter < 20):
            # sum of 20 
            sum += ticker['Close'][i]
        elif (counter == 20):
            # average it
            average = sum/20
            average_list.append(average)
        else:
            #reset sum
            sum = 0
    
    #now iterate through ticker list of close and compare average_list to choose when to buy or sell or nothing
    while(i < len(ticker['Close'])):
        
        print('')

    '''
    read file
    x is average of 20 days of close price
    if b < x < a:
      sell
    if b > x > a:
      buy
    else:
      do nothing
    call backtest
    '''
    print('average')

# testing
BandBounce(choose_date())
