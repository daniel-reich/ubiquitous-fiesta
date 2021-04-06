
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
  def __init__(self, r):
    import math
    self.pi = math.pi
    self.r = r
    
  def getArea(self):
    return self.pi * (self.r**2)
  
  def getPerimeter(self):
    return 2 * (self.pi * self.r)
