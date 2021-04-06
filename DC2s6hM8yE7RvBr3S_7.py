
import numpy as np
​
def subtract_matrix(lst1, lst2):
  a, b = np.array(lst1, dtype=float), np.array(lst2, dtype=float)
  return np.subtract(a, b).tolist()

