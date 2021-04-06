
import numpy as np
​
def get_diagonals(lst):
  mtrx = np.array(lst)
  
  if mtrx.size > 1:
    right_diag = np.diagonal(mtrx).tolist()
    left_diag = np.diagonal(np.fliplr(mtrx)).tolist()
  elif mtrx.size == 0:
    right_diag = left_diag = []
  else:
    right_diag = left_diag = mtrx[0]
​
  return [right_diag, left_diag]

