
import math
class Rectangle:
​
  def __init__(self, sideA=0, sideB=0):
    self.sideA = sideA
    self.sideB = sideB
​
  def getArea(self):
    return self.sideA * self.sideB
  
  def getPerimeter(self):
    return 2 * (self.sideA + self.sideB)
​
class Circle:
​
  def __init__(self, radius = 0):
    self.radius = radius
  
  def getArea(self):
    return math.pi*self.radius**2
    
  def getPerimeter(self):
    return 2*math.pi*self.radius

