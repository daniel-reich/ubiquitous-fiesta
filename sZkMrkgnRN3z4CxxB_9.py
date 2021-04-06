
class Rectangle:
  def __init__(self, x, y, w, h):
    self.x = x
    self.y = y
    self.w = w
    self.h = h
    
  def getedges(self):
    # create a dictionary of all edge coordinates
    top = { (a, self.y) : True for a in range(self.x, self.x+self.w) }
    bot = { (a, self.y+self.h) : True for a in range(self.x, self.x+self.w) }
    lf = { (self.x , a) : True for a in range(self.y, self.y + self.h) }
    rt = { (self.x+self.w , a) : True for a in range(self.y, self.y + self.h) }
    rect = {}
    rect.update(top)
    rect.update(bot)
    rect.update(lf)
    rect.update(rt)
    print(rect)
    return rect.keys()
    
def intersecting(a, b):
  b_coords = b.getedges()
  a_coords = a.getedges()
  for i in b_coords:
    if i in a_coords:
      return True
  return False

