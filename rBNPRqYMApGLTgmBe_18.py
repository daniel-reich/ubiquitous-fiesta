
def combinations(k, n):
    '''
    Returns the number of combinations of k distinct items drawn from n.
    '''
    fact = lambda x: 1 if x < 2 else x * fact(x - 1)
​
    return fact(n) // fact(n - k) // fact(k)   # standard n!/(n-r)!/r!

