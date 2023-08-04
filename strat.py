'''
This file: strat.py
Description: Module contains both Bollinger Band Bounce and Moving Average Crossover strategies
'''
from yf_api import *
from allStrategies import *
    
def give_date(etf_data=yf_api.choose_date('FNGU', '01012020'), e_list=''):
    '''
    Affixes buy/sell signals a date and price in a dictionary
    '''
    c_data = etf_data['Close']
    d_data = etf_data['Date']
    new_list = {}
    i = 0
    while i < len(c_data):
        new_list[d_data[i]] = [c_data[i], e_list[i]]
        i += 1
    return new_list

def check_window(etf_data=yf_api.choose_date('FNGU', '01012020')):
    '''
    Check if the window will fit b/w user chosen date period
    '''
    etf_data = etf_data
    if len(etf_data) <= 20:
        return 5
    elif len(etf_data) > 20:
        return 8
    elif len(etf_data) < 10:
        return 3
    else:
        return 1

class strat(AllStrategies):
    def BandBounce(file=yf_api.choose_date('FNGU', '01012020')):
        '''
        Sends Buy/Sell/Null signals based on whether close market fall out of the standard deviation of the average market price based on a window of days
        '''
        # pull 'close' data
        file = file['Close']

        # Calculate middle, upper, and lower bands
        # Assumes band (std dev) = 2
        # When upper & lower bands squeeze together, good sign to buy/sell cuz will usually expand after
        window = check_window(file)
        mean = file.rolling(window).mean()
        stdDev = file.rolling(window).std()
        uBand = mean + 2 * stdDev
        lBand = mean - 2 * stdDev

        #create list of calls to buy / sell / do nothing
        callist = []
        for n in range(len(file)):
            #print(file[n])
            if file[n] > uBand[n]:     # sell (-1)
                callist.append(-1)
            elif file[n] < lBand[n]:   # buy (1)
                callist.append(1)
            else:                   # do nothing (0)
                callist.append(0)

        #call backtesting module
        return callist

    def MovAvg(etf_data=yf_api.choose_date('FNGU', '01012020')):
        '''Take an average of a window of days and calculate whether the average line is crossed by the market close price'''
        # window is range of indices
        window = check_window(etf_data)
        # i is index
        i = 0
        # iD is distance from index
        iD = 0
        # sum is summation of x indices
        sum = 0
        # average is avg of sum
        average = 0
        # holds the list to compare to close dictionary
        average_list = []
        # first 20 close values append into average_list
        close_data = etf_data['Close']
        while(i < window):
            average_list.append(close_data[i])
            i += 1
        # reset index
        i = 0
        # Average sum of window 
        while(i < len(close_data)):
            if (i + iD == len(close_data)):
                # end average list
                break
            elif (iD < window):
                # sum of 20 
                sum += close_data[i+iD]
                iD += 1
            elif (iD == window):
                average = sum/window
                average_list.append(average)
                average = 0
                sum = 0
                iD = 0
                i += 1
            else:
                print('do nothing')
        # Checks if data points crosses average line. Returns list
        i = 0
        bs_list = [0]
        while (i < len(average_list) - 1):
            if(close_data[i] < close_data[i+1] and close_data[i+1] < average_list[i+1]):
                bs_list.append(-1) # buy
                i+=1
            elif(close_data[i] > close_data[i+1] and close_data[i+1] > average_list[i+1]):
                bs_list.append(1) # sell
                i+=1
            else:
                bs_list.append(0) # do nothing
                i+=1
        return bs_list