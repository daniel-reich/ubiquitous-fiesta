
import math
​
def rectangle_in_circle(w, h, radius):
  return True if 2*radius>=math.sqrt(w**2+h**2) else False

