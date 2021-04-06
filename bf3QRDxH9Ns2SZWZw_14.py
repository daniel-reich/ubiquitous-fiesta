
def all_explode(grid):
  def set_off(r,c):
    d = {'+': [(-1, 0), (0, 1), (1, 0), (0, -1)], 
       'x': [(-1, -1), (-1, 1), (1, 1), (1, -1)]}
    chain = d.get(grid[r][c], [])
    grid[r][c] = '0'
    for i, j in chain:
      if 0<=r+i<len(grid) and 0<=c+j<len(grid[0]):
        set_off(r+i, c+j)
  set_off(0, 0)
  return set(''.join(sum(grid, []))) == {'0'}

