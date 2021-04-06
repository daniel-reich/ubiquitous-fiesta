
class Rectangle:
  def __init__(self, left, top, width, height):
    self.left = left
    self.top = top
    self.right = left + width
    self.bottom = top + height
​
def intersecting(a, b):
  notIntX = a.right < b.left or a.left > b.right
  notIntY = a.bottom < b.top or a.top > b.bottom
  return not(notIntX or notIntY)

