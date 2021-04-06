
import numpy as np
def multiply_matrix(a, b):
  try: return [list(x) for x in np.matmul(np.array(a), np.array(b))]
  except Exception: return "ERROR"

