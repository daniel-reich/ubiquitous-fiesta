
import numpy as np
​
def final(r, c, i):
  matrix = np.zeros((r,c), dtype=np.int8)
  for instruction in i:
    index = int(instruction[0])
    if "r" in instruction:
      matrix[index,:] += 1
    else:
      matrix[:, index] += 1
  return matrix.tolist()

