
class Rectangle:
  def __init__(self, x, y, w, h):
    self.x = x
    self.y = y
    self.w = w
    self.h = h
  
intersecting = lambda a, b: (a.x <= b.x + b.w) and (a.x + a.w >= b.x) and (a.y <= b.y + b.h) and (a.y + a.h >= b.y)

