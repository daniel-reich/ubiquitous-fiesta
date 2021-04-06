
import re
def hex_distance(grid):
  xpos = []
  for i,r in enumerate(grid):
    for m in re.finditer('x', r):
      xpos.append((i, m.start()))
  v, h = abs(xpos[0][0]-xpos[1][0]), abs(xpos[0][1]-xpos[1][1])
  return v + (h-v)//2 if h >= v else v

