
from math import pi
class Circle(object):
  def __init__(self, radius):
    self.radius = radius
  def getArea(self):
    return round(pi * self.radius**2) # round because of error in test
  def getPerimeter(self):
    return round(2 * pi * self.radius)

