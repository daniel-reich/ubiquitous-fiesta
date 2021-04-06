
import math
def distance(t1,t2):
  x1 = t1[0]
  x2 = t2[0]
  y1 = t1[1]
  y2 = t2[1]
  return math.hypot(x1-x2,y1-y2)
def is_parallelogram(lst):
  if distance(lst[0],lst[1]) == distance(lst[2],lst[3]):
    return True
  elif distance(lst[0],lst[2]) == distance(lst[1],lst[3]):
    return True
  elif distance(lst[0],lst[3]) == distance(lst[1],lst[2]):
    return True
  else:
    return False

