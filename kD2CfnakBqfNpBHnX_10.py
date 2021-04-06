
import numpy as np
def islands_perimeter(grid):
  edges = 0
  for k in range(0,2):
    grid = np.rot90(np.array(grid)).tolist()
    edges += grid[0].count(1) + grid[-1].count(1)
    for a,b in zip(grid[:-1],grid[1::]):
      for j in range(0,len(grid[0])):
        if a[j] != b[j]:
          edges += 1
  return edges

