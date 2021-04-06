
def minesweeper(grid):
  rps = [[1,1],[1,0],[1,-1],[0,-1],[-1,-1],[-1,0],[-1,1],[0,1]]
  for x in range(3):
    for y in range(3):
      if grid[x][y] == "?":
        nh = 0
        for rp in rps:
          if 0 <= rp[0]+x < 3 and 0 <= rp[1]+y < 3:
            if grid[rp[0] + x][rp[1] + y] == "#": nh += 1
        grid[x][y] = str(nh)    
​
  return grid

