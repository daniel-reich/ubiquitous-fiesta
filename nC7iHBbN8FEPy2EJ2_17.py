
import math
class Circle:
​
  def __init__(self, radius = 0):
    self.radius = radius 
    
  def getArea(self):
    return math.pi * self.radius * self.radius
  
  def getPerimeter(self):
    return 2 * math.pi * self.radius

