
from itertools import groupby
def daily_streak(lst):
  return len(max(tuple(b) for a,b in groupby(lst) if a)) if True in lst else 0

