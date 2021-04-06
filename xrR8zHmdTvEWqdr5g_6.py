
import math
def returnsides(length):
  triangle = []
  triangle.append(2*length)
  triangle.append(round(length*math.sqrt(3), 2))
  return tuple(triangle)

