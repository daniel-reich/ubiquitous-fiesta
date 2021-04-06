
def funch(lst,count):
    '''
    Returns the number of elements inside lst and any inner lists.
    '''
    for elem in lst:
        count[0] += 1
        if isinstance(elem,list):
            funch(elem,count)
​
    return count[0]
​
def func(lst):
    return funch(lst,[0])

