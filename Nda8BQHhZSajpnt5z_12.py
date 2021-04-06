
from fractions import gcd
from functools import reduce
def GCD(lst):
  x = reduce(gcd,lst)
  return x

