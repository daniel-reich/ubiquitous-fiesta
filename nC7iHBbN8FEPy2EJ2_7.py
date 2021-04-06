
from math import pi
​
class Circle:
  def __init__(self,r):
    self.a=pi*r*r
    self.p=2*pi*r
​
  def getArea(self):
    return self.a
  
  def getPerimeter(self):
    return self.p

