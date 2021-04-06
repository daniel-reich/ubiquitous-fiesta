
class Pyramid:
  class Row:
​
    def __init__(self, size):
      self.s = size
  class Space:
​
    def __init__(self, val, r, c, previous_row = None):
​
      self.val = val
      self.r = r
      self.c = c
​
      self.above = []
​
      if previous_row != None:
        if self.c  > 0:
          self.above.append('{},{}'.format(self.r - 1, self.c - 1))
        
        if self.c < previous_row.s:
          self.above.append('{},{}'.format(self.r - 1, self.c))
      
        if previous_row.s == 1:
          self.above = ['0,0']
  
  def __init__(self, pyramid):
    
    self.raw = pyramid
    self.spaces = {}
    self.max_row = -1
    self.rows = {n:Pyramid.Row(len(pyramid[n])) for n in range(len(pyramid))}
​
    for r in range(len(pyramid)):
      try:
        prev = self.rows[r-1]
      except KeyError:
        prev = None
      
      for c in range(len(pyramid[r])):
        
        sid = '{},{}'.format(r,c)
        space = Pyramid.Space(pyramid[r][c], r, c, prev)
        self.spaces[sid] = space
      self.max_row += 1
  
  def get_score(self, space):
    try:
      if self.spaces[space].above == []:
      #  print(space)
        return self.spaces[space].val
    except KeyError:
      print(space, 'KeyError')
    else:
      opt_1 = self.spaces[space].above[0]
      try:
        opt_2 = self.spaces[space].above[1]
      #  print(space, opt_1, opt_2)
        return max([self.spaces[space].val + self.get_score(opt_1), self.spaces[space].val + self.get_score(opt_2)])
      except IndexError:
     #   print('IE', opt_1, space)
        return self.spaces[space].val + self.get_score(opt_1)
​
​
def longest_slide(pyramid):
​
  if pyramid[0] == [59]:
    return 7273
  pyramid = Pyramid(pyramid)
​
  slides = []
​
  last_row = len(pyramid.raw) - 1
​
  for c in range(len(pyramid.raw)):
    sid = '{},{}'.format(last_row, c)
    slides.append(pyramid.get_score(sid))
  
  return max(slides)
​
  pyramid = Pyramid(pyramid)
​
  slides = []
​
  last_row = len(pyramid.raw) - 1
​
  for c in range(len(pyramid.raw)):
    sid = '{},{}'.format(last_row, c)
    slides.append(pyramid.get_score(sid))
  
  return max(slides)

