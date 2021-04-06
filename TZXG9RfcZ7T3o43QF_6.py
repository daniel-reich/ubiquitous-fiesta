
from itertools import groupby
​
def same_length(txt):
  if len(txt) % 2:
    return False
  groups = [len(list(g)) for k, g in groupby(txt)]
  return all(a == b for a, b in zip(groups[::2], groups[1::2]))

