
import numpy as np
​
def ordered_matrix(a, b):
  lst = np.arange(1, (a*b)+1)
  return lst.reshape(a, b).tolist()

