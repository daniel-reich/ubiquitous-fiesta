
import math
​
def sine(x, y):
  y = math.radians(y)
  return round(x * math.sin(y), 2)
def cosine(x, y):
  y = math.radians(y)
  return round(x * math.cos(y), 2)
def tangent(x, y):
  y = math.radians(y)
  return round(x * math.tan(y), 2)

