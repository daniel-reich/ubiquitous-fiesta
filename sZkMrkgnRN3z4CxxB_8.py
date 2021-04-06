
class Rectangle:
  def __init__(self,x,y,w,h):
    self.x,self.y,self.w,self.h = x,y,w,h
    self.ul = [x,y]
    self.ll = [x,y-h]
    self.ur = [x+w,y]
    self.lr = [x+w,y-h]
​
def intersecting(a, b):
  for i in [a.ul,a.ll,a.ur,a.lr]:
    x,y = i
    if x>=b.ul[0] and y<=b.ul[1]:
      if x>=b.ll[0] and y>=b.ll[1]:
        if x<=b.ur[0] and y<=b.ur[1]:
          if x<=b.lr[0] and y>=b.lr[1]:
            return True
  return False

