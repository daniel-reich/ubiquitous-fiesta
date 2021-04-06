
from functools import reduce
def g(a,b):
    if (b == 0):return a
    return g(b, a % b)
​
def gcd(l):
    return  reduce(g, l)

