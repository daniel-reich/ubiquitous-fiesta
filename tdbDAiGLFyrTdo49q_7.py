
from numpy import prod
​
def product(lst):
  return prod(lst)
​
def find_difference(a, b):
  return abs(product(a) - product(b))

