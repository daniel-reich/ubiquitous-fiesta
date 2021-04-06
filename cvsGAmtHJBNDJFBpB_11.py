
import numpy as np
def can_traverse(x):
  x = np.transpose(x)
  for i in range(len(x) - 1):
    if abs(sum(x[i]) - sum(x[i + 1])) > 1: return False
  return True

