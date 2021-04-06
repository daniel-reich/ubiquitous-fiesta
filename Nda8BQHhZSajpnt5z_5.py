
from fractions import gcd
from functools import reduce
def GCD(lst):
  return reduce(gcd,lst)

