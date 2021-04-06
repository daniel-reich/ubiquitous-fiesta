
def minesweeper(grid):
  for r in range(len(grid)):
    for c in range(len(grid[0])):
      if grid[r][c]=="?":
        tempval=0
        for a,b in [(1,0),(-1,0),(0,1),(0,-1),(1,1),(1,-1),(-1,1),(-1,-1)]:
          if r+a>=0 and c+b>=0 and r+a<len(grid) and c+b<len(grid[0]):
            if grid[r+a][c+b]=="#":
              tempval+=1
        grid[r][c]=str(tempval)
  return grid

