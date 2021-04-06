
def minesweeper(grid):
  for row in range(3):
    for col in range(3):
      if grid[row][col] == '?':
        c = 0
        for i in range(-1, 2):
          for j in range(-1, 2):
            nbr, nbc = row+i, col+j
            if 0 <= nbr < 3 and 0 <= nbc < 3:
              c += grid[nbr][nbc] == '#'
        grid[row][col] = str(c)
  return grid

