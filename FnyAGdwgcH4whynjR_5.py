
from itertools import combinations
def get_subsets(lst, n):
  lst2 = []
  for i in range(1,len(lst)+1):
    f = combinations(lst,i)
    for tpl in f:
      if sum(tpl) == n:
        lst2.append(list(tpl))
  return lst2

