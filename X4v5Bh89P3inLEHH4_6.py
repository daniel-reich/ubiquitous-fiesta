
import math
def spin_around(lst):
  angle = 0
  for turn in lst:
    if turn == "left":
      angle -= 90
    else:
      angle += 90
  return angle//360 if angle//360 >= 0 else abs(math.ceil(angle/360))

