
from functools import reduce
def accumulating_product(lst):
    if not lst : return []
    n_l = [lst[0]]
    for i in range(2,len(lst)+1):
        n_l.append(reduce(lambda x,y:x*y,lst[:i]))
    return n_l

