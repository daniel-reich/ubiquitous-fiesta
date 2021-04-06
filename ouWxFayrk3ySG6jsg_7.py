
import numpy as np
​
def who_won(board):
  b = np.array(board)
  return [l for l in np.r_[b, b.T, [np.diag(b)], [np.diag(np.rot90(b))]] if len(set(l)) == 1][0][0]

