
def group_seats(rows, n):
    '''
    Returns the number of ways a group of n people can sit together in one of
    the rows in rows, as described in the instructions
    '''
    from itertools import groupby
​
    arrangements = [(k, len(list(v))) for row in rows \
                     for k,v in groupby(row)\
                     if k == 0]
    
    return sum(v - n + 1 for _, v in arrangements if v >= n)

