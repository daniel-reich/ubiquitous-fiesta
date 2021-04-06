
import numpy as np
​
def is_wristband(lst):
  lst = np.array(lst)
  rows, cols = len(lst), len(lst[0])
  
  h = all(len(set(i)) == 1 for i in lst)
  v = all(len(set(i)) == 1 for i in lst.T)
  diag_l = all(len(set(np.diag(lst, i))) == 1 for i in range(-rows + 1, cols))
  diag_r = all(len(set(np.diag(np.flip(lst, 1), i))) == 1 for i in range(-rows + 1, cols))
  
  return h or v or diag_l or diag_r

