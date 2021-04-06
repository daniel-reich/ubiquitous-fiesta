
from functools import reduce
​
def boolean_and(lst):
  return reduce(lambda a, b: a and b, lst)
​
def boolean_or(lst):
  return reduce(lambda a, b: a or b, lst)
​
def boolean_xor(lst):
   return reduce(lambda a, b: False if a == b else True, lst)

