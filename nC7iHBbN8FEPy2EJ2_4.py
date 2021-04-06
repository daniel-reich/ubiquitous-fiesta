
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
    pi = 3.141592
    def __init__(self, radius):
        self.radius = radius
​
    def getArea(self):
        return round(Circle.pi*self.radius*self.radius)
​
    def getPerimeter(self):
        return round(2*Circle.pi*self.radius)

