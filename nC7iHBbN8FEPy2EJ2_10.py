
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
  def __init__(self, rad=0):
    self.rad = rad
    
  def getArea(self):
    return math.pi * self.rad**2
    
  def getPerimeter(self):
    return 2 * math.pi * self.rad

