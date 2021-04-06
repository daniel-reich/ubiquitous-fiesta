
import numpy as np
def printgrid(rows, cols):
  arr = np.array(range(1,rows*cols + 1)).reshape(cols,rows)
  return list(map(list,zip(*arr)))

