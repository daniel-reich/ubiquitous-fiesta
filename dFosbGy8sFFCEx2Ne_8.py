
from collections import Counter
def rank(lst):
  ll, slst = len(lst), sorted(lst)
  reps, res, i = dict(Counter(slst)), [], 0
  while i < ll:
    v = lst[i]
    fx, cv = slst.index(v), reps[v]
    rnk = sum(range(fx, fx + cv)) / cv
    while i < ll and  lst[i] == v:
      res.append(rnk)
      i += 1
  return res

