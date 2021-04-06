
import math
def is_circle_collision(c1, c2):
​
  x = c2[1] - c1[1]
  y = c2[2] - c1[2]
  r = c2[0] + c1[0]
  
  d = math.sqrt((x**2) + (y**2))
  if d < r:
    return True
  else:
    return False

