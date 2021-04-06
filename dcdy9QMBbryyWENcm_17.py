
from math import *
​
def total_cups(n):
  div = (n / 6) * 7
  if n >= 6:
    return floor(div)
  else:
    return n

