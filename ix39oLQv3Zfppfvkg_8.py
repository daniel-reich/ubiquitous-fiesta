
import numpy as np
​
def multiply_matrix(m1, m2):
  a, b = np.array(m1), np.array(m2)
  try:
    return np.matmul(a, b).tolist()
  except ValueError:
    return "ERROR"

