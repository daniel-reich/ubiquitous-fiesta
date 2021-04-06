
def islands_perimeter(grid):
  res = 0
  for i in range(len(grid)):
    for j in range(len(grid[0])):
      if grid[i][j]==1:
        res+=neighbors(grid,i,j)
  return res
  
def neighbors(grid,x,y):
  total = 4
  if x-1>=0 and grid[x-1][y]==1:
    total-=1
  if x+1<len(grid) and grid[x+1][y]==1:
    total-=1
  if y-1>=0 and grid[x][y-1]==1:
    total-=1
  if y+1<len(grid[0]) and grid[x][y+1]==1:
    total-=1
  return total

