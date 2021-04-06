
def num_regions(grid):
  def start(a,b):
    if a>=0 and b>=0 and a<len(grid) and b<len(grid[0]):
      if grid[a][b]==0: return 0
      grid[a][b]=0
      for i,j in zip([1,-1,0,0],[0,0,-1,1]):
        start(a+i,b+j)
  
  count=0
  for i in range(len(grid)):
    for j in range(len(grid[0])):
      if grid[i][j]==1:
        count+=1
        start(i,j)
  return count

