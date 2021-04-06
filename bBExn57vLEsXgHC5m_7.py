
import numpy as np
​
​
def same_line(lst):
  x, y, z = lst
  b = np.array([x + [1], y + [1], z + [1]])
  return not np.linalg.det(b)

