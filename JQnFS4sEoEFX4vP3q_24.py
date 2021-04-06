
from itertools import combinations
def product_pair(lst, k):
  ret = [prod(list(c)) for c in combinations(lst,k)]
  return (min(ret),max(ret)) if k<=len(lst) else None
  
def prod(lst):
  ret = 1
  for i in lst: ret*=i
  return ret

