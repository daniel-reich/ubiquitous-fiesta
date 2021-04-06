
from itertools import combinations as comb
def get_subsets(lst, n):
  subs = sum(([list(l) for l in comb(lst,r) if sum(l)==n] for r in range(len(lst)+1)),[])
  return sorted(subs, key = lambda l: (len(l),l))

