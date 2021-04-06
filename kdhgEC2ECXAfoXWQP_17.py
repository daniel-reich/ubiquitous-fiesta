
import numpy as np
def transpose_matrix(mtx):
  n = np.array(mtx)
  return " ".join(n.transpose().flatten())

