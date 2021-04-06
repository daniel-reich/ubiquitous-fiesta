
from itertools import combinations
​
def three_sum(lst):
  res = []
  for i in combinations(lst, 3):
    if not sum(i) and i not in res:
      res.append(i)
  return [list(i) for i in res]

