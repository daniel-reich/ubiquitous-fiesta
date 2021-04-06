
def minesweeper(grid):
  for a in range(3):
    for b in range(3):
      A=[grid[i][j] for i in range(3) for j in range(3) if abs(a-i)<=1 and abs(b-j)<=1]
      if grid[a][b]=='?':
        grid[a][b]=str(A.count('#'))
  return grid

