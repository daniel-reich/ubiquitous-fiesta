
import math
def is_circle_collision(c1, c2):
  dist = math.sqrt((c1[1]-c2[1])**2+(c1[2]-c2[2])**2)
  if dist> c1[0]+c2[0]:
    return False
  elif dist == c1[0]+c2[0]:
    return False
  else:
    return True

