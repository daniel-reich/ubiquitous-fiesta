
import numpy as np
​
def is_magic(square):
  try:
    s = np.array(square)
    l = np.r_[s, s.T, [np.diag(s)], [np.diag(np.rot90(s))]]
    return 1 <= np.min(l) <= np.max(l) <= len(square) ** 2 and np.sum(l, axis=1).ptp() == 0
  except:
    return square == []

