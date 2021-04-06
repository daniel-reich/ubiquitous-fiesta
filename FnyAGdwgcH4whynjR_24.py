
from itertools import combinations
def get_subsets(lst, n):
  ret = []
  for l in range(1,len(lst)+1):
    combs = [comb for comb in combinations(lst,l) if sum(comb) == n]
    for comb in combs:
      ret.append(list(comb))
  return ret

