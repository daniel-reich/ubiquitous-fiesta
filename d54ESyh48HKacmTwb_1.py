
from functools import reduce
def calc(a,b):
  while b:
    a,b = b,a%b
  return a
def gcd(lst):
  return reduce(lambda x,y: calc(x,y),lst)

