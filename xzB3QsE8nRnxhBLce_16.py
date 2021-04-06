
import math
​
def sine(x, y):
  result = x*math.sin(y*math.pi/180)
  return round(result,2)
  
​
def cosine(x, y):
  result = x*math.cos(y*math.pi/180)
  return round(result,2)
  
​
def tangent(x, y):
  result = x*math.tan(y*math.pi/180)
  return round(result,2)

