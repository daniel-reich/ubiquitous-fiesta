
from itertools import combinations
​
def simple_pair(lst, n):
  return [[list(i) for i in combinations(lst, 2) if i[0] * i[1] == n] or [None]][0][0]

