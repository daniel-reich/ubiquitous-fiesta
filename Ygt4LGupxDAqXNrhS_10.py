
from itertools import permutations
def spotlight_map(grid):
  if not grid or not grid[0]:
    return grid
  lg,lg0 = len(grid),len(grid[0])
  dir = set(permutations([1,1,0,0,-1,-1],2))
  return [[sum(grid[i+x][j+y] for x,y in dir if 0 <= i+x < lg and 0 <= j+y < lg0) for j in range(lg0)] for i in range(lg)]

