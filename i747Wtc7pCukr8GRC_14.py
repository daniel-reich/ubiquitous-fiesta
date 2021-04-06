
import numpy as np
from itertools import combinations
def max_product(lst):
  return max(map(np.prod, combinations(lst, 3)))
​
def min_product(lst):
  return min(map(np.prod, combinations(lst, 3)))

