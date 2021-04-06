
def number_of_days(coordinate):
  import math
  xy = abs(coordinate[0]) + abs(coordinate[1])
  return xy + math.ceil(xy/5) -1

