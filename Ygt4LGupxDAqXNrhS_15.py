
def spotlight_map(grid):
  def sums(i,j):
    s = 0
    for a in range(-1,2):
      for b in range(-1,2):
        if min(a+i,b+j) >= 0 and a+i < len(grid) and b+j < len(grid[0]):
          s += grid[a+i][b+j]
    return s
  return [[sums(i,j) for j in range(0,len(grid[0]))] for i in range(0,len(grid))]

