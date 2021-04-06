
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
  import math
  def __init__(self, radius):
    self.radius = radius
    
  def getArea(self):
    import math
    return math.pi * self.radius ** 2
    
  def getPerimeter(self):
    import math
    return math.pi * 2 * self.radius

