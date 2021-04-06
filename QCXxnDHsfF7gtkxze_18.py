
from functools import reduce
def mystery_func(num):
  return reduce(int.__mul__, map(int, str(num)))

