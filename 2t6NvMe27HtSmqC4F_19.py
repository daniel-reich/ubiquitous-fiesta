
from functools import reduce
​
def boolean_and(lst):
  return reduce(lambda a, b : a & b, lst) 
​
def boolean_or(lst):
  return reduce(lambda a, b : a | b, lst) 
​
def boolean_xor(lst):
  return reduce(lambda a, b : a ^ b, lst)

