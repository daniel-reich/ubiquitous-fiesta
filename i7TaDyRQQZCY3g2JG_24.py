
import fractions
from functools import reduce
def lcm1(a, b):
    return a * b // fractions.gcd(a, b)
def lcm(nums):
    return reduce(lcm1, nums)

