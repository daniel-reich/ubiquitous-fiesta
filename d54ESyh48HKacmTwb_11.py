
from fractions import gcd as gcdd
from functools import reduce
def gcd(lst):
  x = reduce(gcdd,lst)
  return x

