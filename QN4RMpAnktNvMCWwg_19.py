
import numpy as np
def id_mtrx(n):
  try:
    return((np.identity(abs(n)),np.rot90(np.identity(abs(n))))[n<0]).tolist()
  except:
    return "Error"

