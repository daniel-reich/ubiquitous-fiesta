
class Rectangle:
  
  def __init__(self, x, y, width, height):
    self.x, self.y = x, y
    self.width, self.height = width, height
​
def intersecting(a, b):
  x = (a.x <= b.x and a.x + a.width >= b.x) or \
    (b.x <= a.x and b.x + b.width >= a.x)
  y = (a.y <= b.y and a.y + a.height >= b.y) or \
    (b.y <= a.y and b.y + b.height >= a.y)
  return x and y

