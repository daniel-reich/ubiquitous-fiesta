
def spotlight_map(grid):
  ret = [[j for j in i] for i in grid]
  for x in range(len(ret)):
    for y in range(len(ret[x])):
      ret[x][y] = checkUpDown(grid,x,y)
  return ret
  
def checkUpDown(grid,x,y):
  ret = grid[x][y]
  ret+=checkLeftRight(grid,x,y)
  if x>0:
    ret+=grid[x-1][y]
    ret+=checkLeftRight(grid,x-1,y)
  if x<len(grid)-1:
    ret+=grid[x+1][y]
    ret+=checkLeftRight(grid,x+1,y)
  return ret
  
def checkLeftRight(grid,x,y):
  ret = 0
  if y>0:
    ret+=grid[x][y-1]
  if y<len(grid[x])-1:
    ret+=grid[x][y+1]
  return ret

