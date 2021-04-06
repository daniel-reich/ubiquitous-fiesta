
import numpy as np
def matrix_multiply(a, b):
  try:
    return np.matmul(a, b).tolist()
  except(ValueError):
    return 'invalid'

