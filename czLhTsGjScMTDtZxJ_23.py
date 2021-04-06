
from functools import reduce
def primorial(n):
  return reduce(lambda x, y: x*y,[2, 3, 5, 7, 11, 13, 17, 19, 23][:n])

