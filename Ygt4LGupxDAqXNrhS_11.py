
def spotlight_map(grid):
  if not grid: return grid
  n,m = len(grid), len(grid[0])
  
  ex_copy = [[0]*m] + [[0]+l+[0] for l in grid] + [[0]*m]
  
  for i in range(n):
    for j in range(m):
      grid[i][j] = sum(sum(l[j:j+3]) for l in ex_copy[i:i+3])
  
  return grid

