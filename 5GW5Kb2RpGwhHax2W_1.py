
import numpy as np
​
def spiral_transposition(lst):
  trans = []
  while len(lst) > 0:
    trans.extend(list(lst[0]))
    lst = np.delete(lst, 0, 0)
    lst = np.rot90(lst)
  return trans

