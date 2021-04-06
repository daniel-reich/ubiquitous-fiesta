
import numpy as np
def rotate(mat):
  return np.rot90(np.array(mat),k=3).tolist()

