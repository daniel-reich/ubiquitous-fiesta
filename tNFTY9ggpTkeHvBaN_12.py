
def total_volume(*boxes):
  import numpy as np
  tot = 0
  for arg in boxes:
    tot = tot + (np.prod(arg))
  return(tot)

