
import math
def is_circle_collision(c1, c2):
  r=c1[0]+c2[0]
  d=math.sqrt((c1[1]-c2[1])**2+(c1[2]-c2[2])**2)
  if d>=r:
    return False
  elif d<r :
    return True

