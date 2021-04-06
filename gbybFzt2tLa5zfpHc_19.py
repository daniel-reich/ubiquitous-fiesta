
from itertools import combinations
def three_sum(lst):
  res = [str(list(i)) for i in combinations(lst,3) if not sum(i)]
  return [eval(i) for i in sorted(set(res),key=res.index)]

