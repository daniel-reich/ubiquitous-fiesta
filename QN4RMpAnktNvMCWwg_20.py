
import numpy as np
​
def id_mtrx(n):
  if type(n) != int:
    return "Error"
  if n > 0:
    return np.eye(n).tolist()
  return np.fliplr(np.eye(-n)).tolist()

