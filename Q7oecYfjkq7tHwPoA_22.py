
from math import ceil
def climb(stamina, obstacles):
  count = 0
  for i in range(1, len(obstacles)):
    stamina -= ceil(abs(obstacles[i] - obstacles[i-1])) * (2 if obstacles[i] > obstacles[i-1] else 1)
    if stamina < 0: return count
    count += 1
  return count

