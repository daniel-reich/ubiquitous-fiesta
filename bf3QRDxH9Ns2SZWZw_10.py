
dx = [(1,1), (1,-1), (-1,1), (-1,-1)]
dp = [(0,1), (1,0), (-1,0), (0,-1)]
​
def all_explode(grid):
  explode(grid, 0, 0)
  return not any(grid[r][c] in 'x+' for r in range(len(grid)) for c in range(len(grid[0])))
  
def explode(grid, r, c):
  if grid[r][c] in 'x+':
    bt, grid[r][c] = grid[r][c], '0'
    for dr, dc in (dx if bt == 'x' else dp):
      if 0<=r+dr<len(grid) and 0<=c+dc<len(grid[0]):
        explode(grid, r+dr, c+dc)
  return

