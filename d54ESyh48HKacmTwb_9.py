
from fractions import gcd as GCD
from functools import reduce
def gcd(lst):
  return reduce(GCD, lst)

