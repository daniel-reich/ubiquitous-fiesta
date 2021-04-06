
from itertools import combinations
def simple_pair(lst, n):
  return next(([x,y] for x,y in combinations(lst,2) if x*y==n),None)

