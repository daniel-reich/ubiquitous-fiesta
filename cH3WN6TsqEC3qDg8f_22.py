
import math
def rectangle_in_circle(w, h, radius):
  a = w ** 2 + h ** 2
  return math.sqrt(a) <= (2 * radius)

