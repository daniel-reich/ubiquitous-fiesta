
from itertools import combinations
def combo(lst, n):
  return [list(t) for t in combinations(lst, n)]

