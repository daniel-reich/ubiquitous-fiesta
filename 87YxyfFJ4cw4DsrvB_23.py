
def generate_rug(n):
  import numpy as np
  center = int((n-1)/2)
  rug = np.array([[0]*n]*n)
  for i in range(1, int((n+1)/2) ):  # for example, if n = 7, i goes from 1 -> 2 -> 3
    for j in range(n):
      rug[center - i, j] = i
      rug[center + i, j] = i
      rug[j, center - i] = i
      rug[j, center + i] = i
  return rug.tolist()

