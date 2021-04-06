
from functools import reduce
gcd = lambda a, b: gcd(b, a % b) if b else a
def GCD(lst):
  return reduce(gcd, lst)

