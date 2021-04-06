
from fractions import gcd
from functools import reduce
lcm_of_list = lambda a: reduce(lambda a, b: a * b // gcd(a, b), a)

