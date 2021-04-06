
from math import pi
​
class Circle():
  def __init__(self, radius):
    self.area = pi * radius ** 2
    self.perimeter = 2 * pi * radius
​
  def getArea(self):
    return self.area
​
  def getPerimeter(self):
    return self.perimeter

