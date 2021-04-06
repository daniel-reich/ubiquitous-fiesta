
import numpy as np
​
def spotlight_map(grid):
  if not grid: return grid
  g = np.array(grid)
  h, w = g.shape
  return [[np.sum(g[max((i-1, 0)):min((i+2, h)), max((j-1, 0)):min((j+2, w))]) for j in range(w)] for i in range(h)]

