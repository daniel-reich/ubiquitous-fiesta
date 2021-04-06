
from math import floor, ceil
​
def climb(stamina, obstacles):
  res=0
  for i in range (len(obstacles)-1):
    if obstacles[i+1] - obstacles[i] < 0:
      stamina += floor(obstacles[i+1] - obstacles[i])
    else:
      stamina -= 2 * ceil(obstacles[i+1] - obstacles[i])
    if stamina < 0:
      return res
    res +=1
  return res

