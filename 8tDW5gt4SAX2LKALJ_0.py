
def min_bombs_needed(grid, i=0):
  def set_off(r,c):
    d = {'+': [(-1, 0), (0, 1), (1, 0), (0, -1)], 
       'x': [(-1, -1), (-1, 1), (1, 1), (1, -1)]}
    chain = d.get(grid[r][c], [])
    grid[r][c] = '0'
    for i, j in chain:
      if 0<=r+i<len(grid) and 0<=c+j<len(grid[0]):
        set_off(r+i, c+j)
  for r in range(len(grid)):
    for c in range(len(grid[0])):
      if grid[r][c] != '0':
        set_off(r, c)
        return min_bombs_needed(grid, i+1)
  return i

