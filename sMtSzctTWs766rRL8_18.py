
import math 
​
def magnitude(lst):
  magnitude = 0
  for coordinate in lst:
    magnitude = magnitude + coordinate*coordinate
  magnitude = math.sqrt(magnitude)
  return magnitude

