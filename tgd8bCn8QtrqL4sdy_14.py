
def minesweeper(grid):
  loc=[[[i,j],len([(k,l) for k in range(i-1,i+1+1) for l in range(j-1,j+1+1) if 0<=k<=2 and 0<=l<=2 if grid[k][l]=="#"])] for i in range(3) for j in range(3) if grid[i][j]=="?"]
  for i in loc:
   grid[i[0][0]][i[0][1]]=str(i[1])
  return grid

