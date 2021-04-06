
import numpy as np
def transpose_matrix(lst):
  a = np.array(lst)
  t = a.transpose()
  return list(map(list,t))

