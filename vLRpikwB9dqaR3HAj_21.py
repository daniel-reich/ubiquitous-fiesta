
from itertools import combinations
​
​
def is_ord_sub(smlst, biglst):
    lista = list(combinations(biglst, len(smlst)))
    return any([list(i) == smlst for i in lista])

