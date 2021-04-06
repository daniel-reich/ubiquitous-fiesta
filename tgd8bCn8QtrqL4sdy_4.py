
flatten = lambda l: [i for sl in l for i in sl]
zero_out = lambda l: [['0' if i == '?' else i for i in sl] for sl in l]
​
# Get surrounding elements of an element in (i,j) of 2D grid
get_surround = lambda l, i, j: [sl[j-1 if j else 0:j+2] for sl in l[i-1 if i else 0:i+2]]
​
def minesweeper(grid):
  if "?" not in flatten(grid):
    return grid
  if "#" not in flatten(grid):
    return zero_out(grid)
    
  for i in range(len(grid)):
    for j in range(len(grid[0])):
      if grid[i][j] == '?':
          grid[i][j] = str(flatten(get_surround(grid, i, j)).count('#'))
      
  return grid

