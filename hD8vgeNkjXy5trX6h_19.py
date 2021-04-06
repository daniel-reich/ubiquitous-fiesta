
from itertools import combinations
def combo(lst, n):
  return [list(item) for item in combinations(lst, n)]

