
def minesweeper(grid):
  for i, m in enumerate(grid):
    for j, n in enumerate(m):
      if n == '?':
        ctr = 0
        for x in range(max(0,i-1), i+2):
          for y in range(max(0,j-1), j+2):
            try: ctr += 1 if grid[x][y] == '#' else 0
            except: pass
        grid[i][j] = str(ctr)
  return grid

