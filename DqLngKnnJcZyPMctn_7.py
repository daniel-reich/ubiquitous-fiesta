
def stock_picker(stocks):
    '''
    Returns the maximum profit by buying and selling the right stock in this
    sequence
    '''
    biggest = max(max(stocks[i+1:])-stocks[i] for i in range(len(stocks)-1))
​
    return (biggest,-1)[biggest<0]

