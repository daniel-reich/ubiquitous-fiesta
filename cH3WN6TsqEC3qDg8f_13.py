
def rectangle_in_circle(w, h, radius):
  from math import pi as pi
  class Rectangle:
  
    def __init__(self, w, h):
      self.w = w
      self.h = h
      
      self.area = w * h
      
      self.c = (w ** 2 +  h ** 2) ** .5
  
  class Circle:
    
    def __init__(self, radius):
      self.r = radius
      
      self.area = pi * (radius ** 2)
    
    def can_fit(self, other):
      
      return self.r >= other.c / 2
      
  
  rectangle = Rectangle(w, h)
  circle = Circle(radius)
  
  return circle.can_fit(rectangle)

