
from itertools import dropwhile
import re
def hex_distance(grid):
  def new_string(i):
    return grid[1][:i] + "x" + grid[1][i+1::]
  grid = list(dropwhile(lambda k: not "x" in k, grid))
  grid = list(dropwhile(lambda k: not "x" in k, grid[::-1]))[::-1]
  if len(grid) == 1:
    try:
      return len(re.findall(r'xo*(?=x)',grid[0].replace(' ',''))[0])
    except IndexError:
      return 0
  if grid[0].index("x") == grid[-1].index("x"):
    return len(grid) - 1
  if grid[0].index("x") == grid[0].index("o") - 1:
    grid[1] = new_string(grid[0].index("x")+1)
  elif not "o" in grid[0][grid[0].index("x")::]:
    grid[1] = new_string(grid[0].index("x")-1)
  elif grid[0].index("x") < grid[-1].index("x"):
    grid[1] = new_string(grid[0].index("x")+1)
  else:
    grid[1] = new_string(grid[0].index("x")-1)
  return 1 + hex_distance(grid[1::])

