
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
def lcm_of_list(*nums):
    return reduce(get_lcm, *nums)

