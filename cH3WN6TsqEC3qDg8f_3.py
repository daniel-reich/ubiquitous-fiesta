
import math
​
def rectangle_in_circle(w, h, radius):
  return float(math.sqrt(((w*0.5)**2)+((h*0.5)**2))) <= float(radius)

