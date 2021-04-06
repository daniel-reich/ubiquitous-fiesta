
import math
​
def lets_meet(distance, va, vb):
  hours = 0
  minutes = 0
  seconds = math.floor(distance / (va + vb) * 3600)
  
  if seconds >= 3600:
    hours = seconds // 3600
    seconds %= 3600
    
  if seconds >= 60:
    minutes = seconds // 60
    seconds %= 60
    
  return str(hours) + "h " + str(minutes) + "min " + str(seconds) + "s"

