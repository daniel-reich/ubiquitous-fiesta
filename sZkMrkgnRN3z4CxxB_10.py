
class Rectangle:
  def __init__(self, x, y, w, h):
    self.x, self.y, self.w, self.h = x, y, w, h
  
  def contains(self, x, y):
    return True if x >= self.x and x <= self.x + self.w and y >= self.y and y <= self.y + self.h else False
​
def intersecting(a, b):
  return a.contains(b.x, b.y) or a.contains(b.x + b.w, b.y) or a.contains(b.x, b.y + b.h) or a.contains(b.x + b.w, b.y + b.h)

