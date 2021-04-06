
import numpy as np
def final(r, c, i):
  arr = np.zeros((r,c), dtype=int)
  for k in i:
    v = int(k[:-1])
    if k[-1] == 'r': arr[v,:] += 1
    if k[-1] == 'c': arr[:,v] += 1
  return arr.tolist()

