
class Rectangle:
  # WRITE CODE HERE.
  def __init__(self, x, y, w, h):
    self.x=x
    self.y=y
    self.w=w
    self.h=h
def intersecting(a, b):
  # WRITE CODE HERE.
  return b.x-a.x<=a.w and b.y-a.y<=a.h

