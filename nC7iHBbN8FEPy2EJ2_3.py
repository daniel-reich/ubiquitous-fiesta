
import math
​
class Circle:
​
  def __init__(self, radius = 0, perimeter = 0):
    self.radius = radius
    self.perimeter = perimeter
    
  def getArea(self):
    return math.pi * math.pow(self.radius, 2)
  
  def getPerimeter(self):
    return 2 * math.pi * self.radius

