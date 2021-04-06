
from itertools import groupby
import math
​
def sock_merchant(lst):
    lst.sort()
    a = [list(a) for b, a in groupby(lst)]
    b = [math.floor(len(i) / 2) for i in a]
​
    return sum(b)

