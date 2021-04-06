
from itertools import combinations 
import functools
def product_pair(lst, k):        
    if k > len(lst):
        return None
    if k == 1:
        resultlist = lst
    else:
        resultlist = ([ functools.reduce(lambda a,b:a*b, list(n)) for n in list(combinations(lst,k)) ])
    return (min(resultlist), max(resultlist))

