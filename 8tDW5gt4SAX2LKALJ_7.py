
dir_h = [(0, 1), (0, -1), (1, 0), (-1, 0)]
dir_d = [(1, 1), (-1, 1), (1, -1), (-1, -1)]
​
def on_grid(grid, r, c):
  return r >= 0 and c >= 0 and r < len(grid) and c < len(grid[0])
​
def set_off_bomb(grid, r, c):
  if grid[r][c] == '0':
    return
  dirs = []
  if grid[r][c] == '+':
    dirs = dir_h
  if grid[r][c] == 'x':
    dirs = dir_d
  grid[r][c] = '0'
  for r2, c2 in [(r+dir[0], c+dir[1]) for dir in dirs if on_grid(grid, r+dir[0], c+dir[1])]:
    set_off_bomb(grid, r2, c2)
​
def min_bombs_needed(grid):
  bombs = 0
  for r in range(len(grid)):
    for c in range(len(grid[0])):
      if grid[r][c] != '0':
        bombs += 1
        set_off_bomb(grid, r, c)
  return bombs

