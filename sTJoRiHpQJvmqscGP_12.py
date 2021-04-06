
from itertools import groupby
​
def daily_streak(lst):
  maxval = 0
  for i, j in groupby(lst):
    if True:
      maxval = max(maxval, sum(j))
  return maxval

