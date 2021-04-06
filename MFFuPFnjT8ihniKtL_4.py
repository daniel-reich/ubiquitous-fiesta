
from math import sqrt
​
def bug_jump(height, time):
  y = -(time/1000 - sqrt(height))**2 + height
  
  half = sqrt(height)
  direction = 'down'
  if time/1000 <= half:
    direction = 'up'
    
  if y > 0:
    return [round(y, 2), direction]
  else:
    return [0, None]

