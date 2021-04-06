
import numpy as np
​
def generate_rug(n):
  i, s = n//2, 0
  arr = np.full((n, n), i)
  while i > 0:
    i, n, s = i-1, n-2, s+1
    arr[s:-s, s:-s] = np.full((n, n), i)
  return arr.tolist()

