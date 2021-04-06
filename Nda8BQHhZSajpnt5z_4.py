
from fractions import gcd
def GCD(lst):
    res = gcd(lst[0], lst[1])
    for x in lst[2:]:
        res = gcd(res, x)
    return res

