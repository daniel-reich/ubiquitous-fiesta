
from collections import defaultdict
def unique(lst):
  d = defaultdict(int)
  for num in lst:
    d[num] += 1
  return min(d, key=lambda x: d[x])

