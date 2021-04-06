
def consecutive_sum(n):
    '''
    Returns whether n is the sum of 2 or more consecutive integers
    '''
    from math import log
    p = log(n,2)
    
    return p != int(p)

