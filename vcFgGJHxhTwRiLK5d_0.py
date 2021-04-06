
from functools import reduce
from fractions import gcd
def smallest(n):
  return reduce(lcm,list(range(1,n+1)))
​
def lcm(x,y):
  return x*y//gcd(x,y)

