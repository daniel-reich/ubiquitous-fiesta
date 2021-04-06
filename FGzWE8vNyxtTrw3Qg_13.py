
def flood_fill(r, c, label, grid):
  grid[r][c] = label
  for r, c in neighbors(r, c, grid):
    if grid[r][c] == 1:
      flood_fill(r, c, label, grid)
​
def neighbors(r, c, grid):
  lst = []
  offsets = [(-1, 0), (0, -1), (0, 1), (1, 0)]
  height = len(grid)
  width = len(grid[0])
  for i, j in offsets:
    ri = r + i
    cj = c + j 
    if not (i == 0 and j == 0) and ri >= 0 and ri < height and cj >= 0 and cj < width:
      lst.append((ri, cj))
  return lst
            
def num_regions(grid):
  label= 1
  for r in range(len(grid)):
    for c in range(len(grid[0])):
      if grid[r][c] == 1:
        label += 1
        flood_fill(r, c, label, grid)
  return len(set([i for r in grid for i in r])) - 1

