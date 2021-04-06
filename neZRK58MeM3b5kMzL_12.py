
import math 
def height_needed(volume):
  radius = 5
  height = 3 * (volume/(math.pi*math.pow(radius, 2)))
  return round(1000*height,2)

