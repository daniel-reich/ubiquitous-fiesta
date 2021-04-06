
def combo(lst, n):
  from itertools import combinations
  return [list(x) for x in combinations(lst,n)]

