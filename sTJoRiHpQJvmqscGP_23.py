
from itertools import groupby
def daily_streak(lst):
  g = [len(list(group)) for x,group in groupby(lst) if x]
  return max(g) if g else 0

