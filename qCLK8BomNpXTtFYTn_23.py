
import itertools
​
def cumulative_sum(lst):
  if not lst:
    return []
  if len(lst) == 1:
    return lst
  return  list(itertools.accumulate(lst))

