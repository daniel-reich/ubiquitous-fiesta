
def min_bombs_needed(grid):
    count=0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] in ['+','x']:
                active(i,j,grid)
                count+=1
    return count
  
def active(x,y,grid):
    if grid[x][y]=='+':
        grid[x][y]=True
        try:active(x+1,y,grid)
        except:pass
        if x-1>=0:active(x-1,y,grid)
        try:active(x,y+1,grid)
        except:pass
        if y-1>=0:active(x,y-1,grid)
    if grid[x][y]=='x':
        grid[x][y]=True
        try:active(x+1,y+1,grid)
        except:pass
        if x-1>=0 and y-1>=0:active(x-1,y-1,grid)
        if x-1>=0 and y+1<len(grid[0]):active(x-1,y+1,grid)
        if y-1>=0 and x+1<len(grid):active(x+1,y-1,grid)

