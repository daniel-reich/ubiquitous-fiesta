
from itertools import combinations
​
def get_subsets(lst, n):
  return [list(i) for l in range(len(lst) + 1) for i in combinations(lst, l) if sum(i) == n]

