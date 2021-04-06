
from functools import reduce
​
def get_gcd(a, b):
    while b:
        a, b = b, a%b
    return a
​
def get_lcm(a, b):
    return a*b // get_gcd(a, b)
​
def smallest(n):
    return reduce(get_lcm, range(1, n+1))

