
from itertools import groupby
​
def landscape_type(lst):
  lst = [k for k, _ in groupby(lst)]
  change = [b > a for a, b in zip(lst, lst[1:])]
  groups = [k for k, _ in groupby(change)]
  
  if groups == [True, False]:
    return 'mountain'
  elif groups == [False, True]:
    return 'valley'
  return 'neither'

