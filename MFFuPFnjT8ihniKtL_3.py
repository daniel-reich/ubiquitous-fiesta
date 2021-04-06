
import math
def bug_jump(height, time):
  t = float(time)/1000
  c = 2 * math.sqrt(height)
  d = t * (c - t)
  if d < 0:
    return([0, None])
  
  if t < c/2:
    return([round(d,2), "up"])
  else:
    return([round(d,2), "down"])

