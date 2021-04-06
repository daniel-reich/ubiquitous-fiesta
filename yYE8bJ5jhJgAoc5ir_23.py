
import numpy as np
def bugger(num):
  if len(str(num)) == 1:
    return 0
  return 1 + bugger(np.prod(np.array([int(x) for x in str(num)])))

