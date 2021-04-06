
from itertools import combinations
def combo(lst, n):
  
​
  if n > len(lst): return []
  return [list(x) for x in combinations(lst, n)]

