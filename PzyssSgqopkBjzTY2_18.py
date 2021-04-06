
import sys
sys.setrecursionlimit(20000)
​
def can_exit(lst, pos=(0, 0), last_pos=None):
  width, height = len(lst[0]), len(lst)
  x, y = pos
  
  if x == width - 1 and y == height - 1:
    return True
  
  surroundings = [
    (x + xoffset, y + yoffset)
      for xoffset in range(-1, 2)
      for yoffset in range(-1, 2)
      if x + xoffset in range(0, width)
      and y + yoffset in range(0, height)
      and abs(xoffset) + abs(yoffset) == 1
      and (x + xoffset, y + yoffset) != last_pos
      and lst[y + yoffset][x + xoffset] == 0
  ]
  
  if surroundings == []:
    return False
  
  return any(can_exit(lst, coord, pos) for coord in surroundings)

