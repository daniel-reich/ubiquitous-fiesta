
def spotlight_map(grid):
  if not grid: return grid
  w, h = len(grid[0]), len(grid)
  sum_spot = lambda r,c: sum(grid[r+dr][c+dc] for dr in range(-1,2) for dc in range(-1,2) if 0<=r+dr<h and 0<=c+dc<w)
  return [[sum_spot(r,c) for c in range(w)] for r in range(h)]

