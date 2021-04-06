
from itertools import combinations
​
def check_sum(lst, n):
  return any(sum(i) == n for i in combinations(lst, 2))

