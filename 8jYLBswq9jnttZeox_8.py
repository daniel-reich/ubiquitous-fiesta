
def langtons_ant(grid, x, y, n, d=0):
  for i in range(n):
    if d==0:
      if grid[x][y]==1:
        d+=1
      elif grid[x][y]==0:
        d=3
    elif d==1:
      if grid[x][y]==1:
        d+=1
      elif grid[x][y]==0:
        d-=1
    elif d==2:
      if grid[x][y]==1:
        d+=1
      elif grid[x][y]==0:
        d-=1
    elif d==3:
      if grid[x][y]==1:
        d=0
      elif grid[x][y]==0:
        d-=1
    grid,x,y = move(grid,x,y,d)
  return grid
        
def move(grid,x,y,d):
  if d==0:
    a,b = -1,0
  elif d==1:
    a,b = 0,1
  elif d==2:
    a,b = 1,0
  elif d==3:
    a,b = 0,-1
  if grid[x][y]==1: grid[x][y]=0
  else: grid[x][y]=1
  if 0<=x+a<len(grid) and 0<=y+b<len(grid[x]):
    return grid,x+a,y+b
  elif x+a<0:
    grid = ([[0] * len(grid[x])])+grid
    return grid,x,y
  elif x+a==len(grid):
    grid = grid + ([[0] * len(grid[x])])
    return grid,x+a,y+b
  elif y+b<0:
    grid = [[0]+i for i in grid]
    return grid,x,y
  elif y+b==len(grid[x]):
    grid = [i+[0] for i in grid]
    return grid,x+a,y+b

