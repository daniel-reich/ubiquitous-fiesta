
import math
​
class Circle:
​
  def __init__(self, radius):
    self.radius = radius
    self.area = math.pi * math.pow(radius, 2)
    self.circumference = 2 * math.pi * radius
​
  def getArea(self):
    return self.area
  
  def getPerimeter(self):
    return self.circumference

