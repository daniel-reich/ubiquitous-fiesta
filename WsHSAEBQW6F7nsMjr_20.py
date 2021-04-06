
from statistics import mean
def flatten_the_curve(lst):
  if len(lst) == 0:
    return lst
  m = mean(lst)
  res = []
  for x in lst:
    res.append(round(m,1))
  return res

