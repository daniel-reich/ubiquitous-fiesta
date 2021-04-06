
import itertools
​
def get_prod(A):
    p = 1
    for a in A:
        p *= a
    return p
​
def product_pair(lst, k):
    if len(lst) < k:
        return 
    low, high = 2**31, -2**31
    for comb in itertools.combinations(lst, k):
        p = get_prod(comb)
        low = min(low, p)
        high = max(high, p)
    return (low, high)

