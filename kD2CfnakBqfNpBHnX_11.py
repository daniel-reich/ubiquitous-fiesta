
def islands_perimeter(grid):
  ret = 0
  for x in range(len(grid)):
    for y in range(len(grid[x])):
      if grid[x][y]==1:
        if x==0:
          ret+=1
        if y==0:
          ret+=1
        if x>0 and grid[x-1][y]==0:
          ret+=1
        if y>0 and grid[x][y-1]==0:
          ret+=1
        if x<len(grid)-1 and grid[x+1][y]==0:
          ret+=1
        if y<len(grid[x])-1 and grid[x][y+1]==0:
          ret+=1
        if x==len(grid)-1:
          ret+=1
        if y==len(grid[x])-1:
          ret+=1
  return ret

