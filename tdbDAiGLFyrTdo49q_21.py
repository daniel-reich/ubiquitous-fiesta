
from functools import reduce
def find_difference(a, b):
  prod = lambda lst: reduce(int.__mul__, lst)
  return abs(prod(a) - prod(b))

