
dir_h = [(0, 1), (0, -1), (1, 0), (-1, 0)]
dir_d = [(1, 1), (-1, 1), (1, -1), (-1, -1)]
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
  for r2, c2 in [(r+dir[0], c+dir[1]) for dir in dirs if 0<=r+dir[0]<len(grid) and 0<=c+dir[1]<len(grid[0])]:
    set_off_bomb(grid, r2, c2)
​
def all_explode(grid):
  set_off_bomb(grid, 0, 0)
  for r in range(len(grid)):
    for c in range(len(grid[0])):
      if grid[r][c] != '0':
        return False
  return True

