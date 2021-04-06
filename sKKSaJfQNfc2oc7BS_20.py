
import numpy as np
def sle(m):
  m = np.array(m)
  try:
    r = tuple(round(n) for n in np.linalg.solve(m[:, :2], m[:,2]))
  except np.linalg.LinAlgError:
    r = False
  return r

