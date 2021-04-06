
from math import *
​
def digits(n):
  p = ceil(log10(n))
  return n * p + (1 - 10 ** p) // 9

