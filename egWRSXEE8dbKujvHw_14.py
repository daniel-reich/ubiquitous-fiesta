
import math
def is_circle_collision(c1, c2):
  def distance(x, y, x1, y1):
    dx = x - x1
    dy = y - y1
    sqdist = ((dx ** 2) + (dy ** 2))
    return math.sqrt(sqdist)
    
  dr = c1[0] + c2[0]
  dist = distance(c1[1], c1[2], c2[1], c2[2])
  
  if(dist <= dr):
    return True
  return False

