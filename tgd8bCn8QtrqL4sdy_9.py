
def minesweeper(grid):
  for y in range(3):
    for x in range(3):
      if grid[y][x] == "?":
        minecount = 0
        for yoffset in [y-1,y,y+1]:
          for xoffset in [x-1,x,x+1]:
            if yoffset>=0 and xoffset>=0 and yoffset<=2 and xoffset<=2:
              if grid[yoffset][xoffset] == "#":
                minecount += 1
        grid[y][x] = str(minecount)
  return grid

