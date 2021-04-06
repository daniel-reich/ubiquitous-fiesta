
import math
def height(side):
  string = ""
  height = 1/2 * math.sqrt(3) * side
  height *= 10
  height = round(height, 1)
  string += str(height) + " mm"
  return string

