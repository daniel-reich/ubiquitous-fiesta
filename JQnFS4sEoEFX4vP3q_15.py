
def product_pair(lst, k):
    '''
    Returns the minimum and maximum products of k elements from lst, or None
    if this is not possible
    '''
    from itertools import combinations
    from functools import reduce
​
    if k > len(lst):
        return None
​
    multiply = lambda c: reduce(lambda x,y:x*y,c,1)
    minimum, maximum = float('inf'), float('-inf')
​
    for combo in combinations(lst, k):
        product = multiply(combo)
        if product < minimum:
            minimum = product
        if product > maximum:
            maximum = product
​
    return (minimum, maximum)

