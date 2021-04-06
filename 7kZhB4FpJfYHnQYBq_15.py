
from functools import reduce
def gcdFunc(m,n):
  num = m
  den = n
  rem = m % n
  while rem:
    num = den
    den = rem
    rem = num % den
  return den    
    
def lcmFunc(m, n):
  return (m * n ) / gcdFunc(m,n)
​
def lcm_three(given_list_3):
  return reduce(lcmFunc, given_list_3)

