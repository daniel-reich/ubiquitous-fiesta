
from functools import reduce
​
def persistence(n):
  r = 0
  while n > 9:
    n = reduce(lambda a,b: a * int(b), str(n), 1)
    r += 1
  return r

