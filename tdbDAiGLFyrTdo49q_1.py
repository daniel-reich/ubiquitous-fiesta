
from functools import reduce
def volume(lst):
  return reduce(lambda a, b: a * b, lst)
​
def find_difference(a, b):
  return abs(volume(a) - volume(b))

