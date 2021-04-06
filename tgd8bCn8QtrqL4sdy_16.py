
def minesweeper(grid):
  for y in range(len(grid)):
    for x in range(len(grid[y])):
      if grid[y][x]=='?':
        grid[y][x] = checkLeftRight(grid,y,x)+checkUpDown(grid,y,x)+checkDiag(grid,y,x)
        grid[y][x]=str(grid[y][x])
  return grid
  
def checkLeftRight(grid,y,x):
  ret = 0
  if x>0 and grid[y][x-1]=='#':
    ret+=1
  if x<len(grid[y])-1 and grid[y][x+1]=='#':
    ret+=1
  return ret
​
def checkUpDown(grid,y,x):
  ret = 0
  if y>0 and grid[y-1][x]=='#':
    ret+=1
  if y<len(grid)-1 and grid[y+1][x]=='#':
    ret+=1
  return ret
  
def checkDiag(grid,y,x):
  ret = 0
  if y>0:
    ret+=checkLeftRight(grid,y-1,x)
  if y<len(grid)-1:
    ret+=checkLeftRight(grid,y+1,x)
  return ret

