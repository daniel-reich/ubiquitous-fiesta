
from itertools import groupby
def landscape_type(lst):
  up = [a < b for a, b in zip(lst, lst[1:]) if a != b]
  if len(list(groupby(up))) == 2:
    return 'mountain' if up[0] else 'valley'
  return 'neither'

