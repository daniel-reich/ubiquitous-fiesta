
from functools import reduce
def lcm(nums):
  return reduce(lambda n, m: (n*m)/gcd(n,m),nums,1)
  
def gcd(x,y):
  while y:
    x, y = y, x%y
  return x

