
from math import log
​
def only5and3(n):
  while n >= 0:
    if n!= 1 and (n == 0 or log(n, 3).is_integer()): return True
    n -= 5
  return False

