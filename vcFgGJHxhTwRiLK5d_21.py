
from fractions import gcd
​
def smallest(n):
    l = 1
    for x in range(1, n+1):
        l = lcm(l, x)
    return l
​
def lcm(a, b):
    return a * b // gcd(a, b)

