
from functools import *
def root_digit(n):
  x = reduce(lambda x, y: int(x) + int(y), str(n))
  while len(str(x)) > 1:
      x = reduce(lambda x, y: int(x) + int(y), str(x))
  return int(x)

