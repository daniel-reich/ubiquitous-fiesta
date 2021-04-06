
from functools import reduce
def lcm_of_list(r):
  gcd = lambda a, b: gcd(b, a % b) if b else a
  return reduce(lambda x, y: x*y//gcd(x, y), r)

