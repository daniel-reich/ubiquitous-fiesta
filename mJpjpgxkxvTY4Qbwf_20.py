
import numpy as np
​
def bingo_check(board):
  b = np.array(board)
  lines = np.r_[b, b.T, [np.diag(b)], [np.diag(np.rot90(b))]]
  return any(set(x) == {"x"} for x in lines)

