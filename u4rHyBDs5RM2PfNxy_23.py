
import itertools
​
def count_ones(lst):
  s = 0
  lst = [str(i) for i in lst]
  for k, g in itertools.groupby(lst):
    status = (sum(1 for x in list(g)) > 1 and k == '1')
    if status:
      s += 1
  return s

