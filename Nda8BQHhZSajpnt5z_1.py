
from functools import reduce
def GCD(lst):
  return reduce(gcd, lst)
  
def gcd(x, y):
  while y:
    x, y = y, x%y
  return x

