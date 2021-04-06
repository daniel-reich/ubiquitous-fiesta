
from functools import reduce
​
def get_products(lst):
    L = []
    for z in lst:
        tmp = lst[:]
        tmp.remove(z)
        L.append(reduce(lambda x, y: x*y, tmp))
    return L

