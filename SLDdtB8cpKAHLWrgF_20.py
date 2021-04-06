
from itertools import permutations as perms
def greater_permutation(expr, nums):
    v, e = max([f(expr, p) for p in perms(nums)])
    if int(v) == v:
        v = int(v)
    return e + ' = ' + str(v)
    
def f(e, p):
    a, b, c = p
    e = e.replace('a', str(a))
    e = e.replace('b', str(b))
    e = e.replace('c', str(c))
    return round(eval(e), 2), e

