
import math
def bug_jump(height, time):
​
  mid = math.sqrt(height)
  time_f = mid * 2000
​
  y = -(time/1000 - mid)**2 + height
  y = 0 if y < 0 else round(y,2)
  if y == 0 and round(time_f) != time:
    return [y,None]
  return [y,'up'] if time < mid*1000 else [y,'down']

