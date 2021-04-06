
from collections import Counter
def unique(lst):
  h = Counter(lst)
  for k,v in h.items():
    if v == 1:
      return k

