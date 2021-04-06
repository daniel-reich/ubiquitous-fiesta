
def minesweeper(grid):
  d=((-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1))
  return [[grid[i][j]  if grid[i][j]!='?' else str(sum([grid[i+y][j+x]=='#' for x,y in d if 0<=i+y<len(grid) and 0<=j+x<len(grid[0])])) for j in range(len(grid[0]))]for i in range(len(grid))]

