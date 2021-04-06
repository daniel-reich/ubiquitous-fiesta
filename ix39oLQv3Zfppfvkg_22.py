
import numpy as np
​
def multiply_matrix(m1, m2):
  try:
    return np.dot(m1, m2).tolist()
  except:
    return "ERROR"

