
from itertools import combinations as comb
​
def get_subsets(lst, n):
  return [list(c) for i in range(1, len(lst) + 1) for c in comb(lst, i) if sum(c) == n]

