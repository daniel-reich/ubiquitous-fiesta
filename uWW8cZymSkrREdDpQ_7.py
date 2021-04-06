
from itertools import combinations as cb
def sums_up(lst):
  return {'pairs':sorted([sorted(list(x)) for x in cb(lst,2) if sum(x)==8],key=lambda x: max(lst.index(x[0]),lst.index(x[1])))}

