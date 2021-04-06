
import math
​
def rectangle_in_circle(w, h, radius):
  # a**2 + b**2 = c**2 --> Pythagorean Theorem, solve for c
  c_squared = math.sqrt(w**2 + h**2)
  # c_squared is the diameter, so need to compare it to radius * 2
  if c_squared <= radius * 2:
    return True
  else:
    return False

