
def islands_perimeter(grid):
  grid = [[0]+row+[0] for row in grid]
  grid = [[0]*len(grid[0])] + grid + [[0]*len(grid[0])]
  return sum(abs(grid[i][j] - grid[i-1][j]) + abs(grid[i][j]-grid[i][j-1]) for i in range(1,len(grid)) for j in range(1,len(grid[0])))

