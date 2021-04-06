
import numpy as np
def matrix_mult(m1, m2):
  a, b = np.array(m1), np.array(m2)
  return [list(i) for i in a.dot(b)]

