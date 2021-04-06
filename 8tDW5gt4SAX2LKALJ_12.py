
from itertools import dropwhile
def min_bombs_needed(grid):
  if "+" in grid[0]:
    char = "+"
    lst1,lst2 = [-1,0,0,1],[0,-1,1,0]
  else:
    char = "x"
    lst1,lst2 = [-1,-1,1,1],[-1,1,-1,1]
  def valid(i,j):
    try: return grid[i][j] == char if min(i,j) >= 0 else False
    except IndexError: return False
  def neighbors(i,j):
    return [(i+a,j+b) for a,b in zip(lst1,lst2) if valid(i+a,j+b)]
  total = 0
  while grid:
    start = (0,grid[0].index(char))
    queue = [start]
    while queue:
      current = queue[0]
      queue.extend(neighbors(current[0],current[1]))
      for point in queue:
        grid[point[0]][point[1]] = "0"
      queue.pop(0)
    total += 1
    grid = list(dropwhile(lambda x: not char in x, grid))
  return total

