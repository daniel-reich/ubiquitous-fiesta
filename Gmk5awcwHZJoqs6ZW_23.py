
from itertools import product
​
def get(lst, coord):
  x, y = coord
  return lst[y][x]
​
def get_island(lst, coord, width, height, seen, rtn=None):
  if rtn is None:
    rtn = []
  rtn.append(coord)
  x, y = coord
  neighbours = ((x, y+1), (x, y-1),
    (x+1, y+1), (x+1, y), (x+1, y-1),
    (x-1, y+1), (x-1, y), (x-1, y-1))
  neighbours = [(a,b) for a, b in neighbours
    if (0 <= a < width) and (0 <= b < height)]
  for neighbour in neighbours:
    if neighbour in seen:
      continue
    seen.add(neighbour)
    if not get(lst, neighbour):
      continue
    get_island(lst, neighbour, width, height, seen, rtn)
  return rtn
​
​
def largest_island(lst):
  height = len(lst)
  width = len(lst[0])
  seen = set()
  islands = []
  for coord in product(range(width), range(height)):
    if coord in seen:
      continue
    seen.add(coord)
    if not get(lst, coord):
      continue
    islands.append(get_island(lst, coord, width, height, seen))
  return max(len(island) for island in islands)

