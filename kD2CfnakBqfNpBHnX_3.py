
import numpy as np
def islands_perimeter(grid):
  a = np.array(grid)
  a = np.pad(a, (1, 1), 'constant', constant_values=(0, 0))
  cc = 0
​
  for i in range(1,a.shape[0]-1):
      for j in range(1,a.shape[1]-1):
          if a[i][j]==1:
              cc -= ((a[i][j-1]+a[i][j+1]+a[i-1][j]+a[i+1][j])-4)
  return cc

