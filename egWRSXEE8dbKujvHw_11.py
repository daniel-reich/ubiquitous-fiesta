
import math
def is_circle_collision(c1, c2):
  return dist(c1[1],c1[2],c2[1],c2[2]) < c1[0] + c2[0]
def dist(x1,y1,x2,y2):
  return math.sqrt((x2 - x1)**2 + (y2-y1)**2)

