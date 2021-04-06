
from math import sqrt
def right_triangle(x, y, z):
  if x<=0 or y<=0 or z<=0:
    return False
  l=sorted([x,y,z])
  return l[-1]==sqrt(l[0]**2+l[1]**2)

