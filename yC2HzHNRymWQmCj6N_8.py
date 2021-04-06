
def less_or_equal(lst1,k):
    '''
    Returns the smallest positive integer x so that k elements in lst are less
    than or wqual to it or None if this is not possible
    '''
    lst, size = sorted(lst1), len(lst1)
    target = lst[k-1] if k > 0 else 1
    checker = lst[k] if k < size else float('inf')
​
    return (None, target)[checker > target]

