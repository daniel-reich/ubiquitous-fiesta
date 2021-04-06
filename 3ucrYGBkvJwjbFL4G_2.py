
helper = lambda start,stop, inc: [start] + ([] if start == stop else \
                                            helper(start+inc,stop,inc))
​
def reversible_inclusive_list(start, stop):
    '''
    Returns a list of the numbers between start and stop inclusive
    '''
    return helper(start, stop, inc=1 if start <= stop else -1)

