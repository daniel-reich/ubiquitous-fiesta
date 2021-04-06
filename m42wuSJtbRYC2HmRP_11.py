
def largest_exponential(values):
    '''
    Each number in the values list is a (num, exponential) pair. This function
    returns the index (from 1) of the number with the highest value.
    '''
    from math import log
​
    log_vals = [b * log(a,10) for a,b in values]
    return log_vals.index(max(log_vals)) + 1

