
from itertools import combinations
def simple_pair(lst, n):
  r_lst=[x for x in combinations(lst,2) if x[0]*x[1]==n]
  return list(r_lst[0]) if r_lst else None

