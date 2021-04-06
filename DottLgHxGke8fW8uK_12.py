
from functools import reduce
​
def nPr(n, r):
    return reduce(lambda x, y: x*y, [i for i in range(n, n-r, -1)])
​
def nCr(n, r):
    a, b, c = min(r, n-r), max(r, n-r), 1
    for i in range(1, a+1):
        c *= (i+b)/i
    return round(c)

