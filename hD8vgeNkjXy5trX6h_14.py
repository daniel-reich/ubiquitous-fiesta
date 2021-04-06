
from itertools import combinations
def combo(lst, n):
  return [list(comb) for comb in combinations(lst,n)]

