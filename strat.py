#module contains both Bollinger Band Bounce and Moving Average Crossover
from yf_api import choose_date


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
    return callist

# use 20 days as data points
def MovAvg(etf_data=choose_date(), window=20):
    '''Take an average of a period of days and calculate whether the average line is crossed by the market close price'''
    # window is range of indices
    window = window
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
    while(i < window):
        average_list.append(etf_data['Close'][i])
        i += 1
    # reset index
    i = 0

    # should iterate starting from 0, and summate 20 indices and calculate avg 
    # logic check needed: if 20 values are in avg list, and after x is averaged after 20 indices, and that average is appended to the end
    # of the average_list, the first value of average corresponds with 0. The average of etf_data indices 0 to 19 will correspond to average_list[0]. 
    # Thus len(etf_data['Close']) - 20 to len(etf_data['Close']) will correspond to average_list[len(average_list)-1]
    # This would mean that etf_data['Close'] are of equal length to average_list
    while(i < len(etf_data['Close'])):
        if (i + iD == len(etf_data['Close'])):
            # end average list
            break
        elif (iD < window):
            # sum of 20 
            sum += etf_data['Close'][i+iD]
            iD += 1
        elif (iD == window):
            # average it
            #reset sum and iD and increment i by 1
            average = sum/window
            average_list.append(average)
            average = 0
            sum = 0
            iD = 0
            i += 1
        else:
            print('do nothing')

    
    #now iterate through ticker list of close and compare average_list to choose when to buy or sell or nothing
    '''
    b = previous point in etf_data
    x = next point in etf_data
    a = x point in average_list
    if b < x < a:
      sell
    if b > x > a:
      buy
    else:
      do nothing
    call backtest
    '''
    # later returns buy/sell list
    return average_list

# testing
#print(BandBounce(choose_date('FNGD', '05012022')))



t = choose_date('FNGD', '05012023')
avg_list = MovAvg(t)
c_list = t['Close']
counter = 0

print(avg_list)
print(c_list)

'''
print('Close Dates')
while(counter < len(c_list['Close'])):
    print(str(c_list['Close'][counter]) + ' : ' + str(avg_list[counter])) 
    counter += 1
'''