
from copy import deepcopy
​
def almost_sorted(lst):
  if lst == sorted(lst) or lst == sorted(lst, reverse = True):
    return False 
  for i in range(len(lst)):
    l = deepcopy(lst)
    l.pop(i)
    if l == sorted(l) or l == sorted(l, reverse = True):
      return True 
  return False

