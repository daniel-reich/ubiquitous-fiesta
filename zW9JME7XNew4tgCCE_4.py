
def reversible_inclusive_list(start, stop):
    '''
    Returns a list of the numbers between start and stop inclusive
    '''
    step = 1 if stop >= start else -1
​
    return list(range(start, stop+step, step))

