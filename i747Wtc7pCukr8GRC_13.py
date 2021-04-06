
from itertools import combinations
​
result = lambda f, x: f(a*b*c for (a,b,c) in combinations(x, 3))
​
def max_product(numbers):
    '''
    Returns the maximum product of 3 numbers in list numbers
    '''
    return result(max, numbers)
​
def min_product(numbers):
    '''
    Returns the minimum product of 3 numbers in list numbers
    '''
    return result(min, numbers)

