
from itertools import combinations
import numpy
​
def product_pair(lst, k):
  if k > len(lst):
    return None
  x = combinations(lst, k)
  y = [numpy.prod(item) for item in x]
  return (min(y), max(y))

