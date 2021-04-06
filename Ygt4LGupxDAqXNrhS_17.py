
def spotlight_map(grid):
  res = [[0 for i in range(len(grid[0]))] for j in range(len(grid))]
  for i in range(len(grid)):
    for j in range(len(grid[i])):
      res[i][j] = around(grid,i,j)+grid[i][j]
  return res
  
def around(arr,x,y):
  total = 0
  if x-1>-1:
    total+=arr[x-1][y]
  if x-1>-1 and y-1>-1:
    total+=arr[x-1][y-1]
  if x-1>-1 and y+1<len(arr[0]):
    total+=arr[x-1][y+1]
  if x+1<len(arr):
    total+=arr[x+1][y]
  if x+1<len(arr) and y-1>-1:
    total+=arr[x+1][y-1]
  if x+1<len(arr) and y+1<len(arr[0]):
    total+=arr[x+1][y+1]
  if y-1>-1:
    total+=arr[x][y-1]
  if y+1<len(arr[0]):
    total+=arr[x][y+1]
  return total

