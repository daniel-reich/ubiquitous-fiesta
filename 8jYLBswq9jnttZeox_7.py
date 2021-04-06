
def langtons_ant(grid, column, row, n, direction=0):
​
  for i in range(n):
    #print(column,row)
    
    if grid[row][column]==1:
      direction=(direction+1)%4
      grid[row][column]=0
    else:
      direction=(direction-1)%4
      grid[row][column]=1
    if direction==0: row-=1
    if direction==2: row+=1
    if direction==1: column+=1
    if direction==3: column-=1
    
    
    if column>=len(grid[0]):
      grid=[x+[0] for x in grid]
    if column<0:
      grid=[[0]+x for x in grid]
      column+=1
    if row>=len(grid):
      grid= grid+ [[0 for x in grid[0] ]]
    if row<0:
      grid= [[0 for x in grid[0] ]] + grid
      row+=1
​
  
  return grid

