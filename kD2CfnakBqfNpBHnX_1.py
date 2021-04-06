
def islands_perimeter(grid):
  a = sum(grid[0]) + sum(grid[-1])
  b = sum(x[0] + x[-1] for x in grid)
  c = sum(row[x] != row[x+1] for row in grid for x in range(len(row)-1))
  d = sum(grid[x][y] != grid[x+1][y] for x in range(len(grid)-1) for y in range(len(grid[x])))
  return a+b+c+d

