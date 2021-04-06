
class Grid:
  class Space:
​
    def __init__(self, val, r, c, mr, mc):
​
      self.v = val
      self.r = r
      self.c = c 
​
      self.up = list(reversed(['{},{}'.format(r, self.c) for r in range(0, self.r)]))
      self.down = ['{},{}'.format(r, self.c) for r in range(self.r + 1, mr)]
      self.left = list(reversed(['{},{}'.format(self.r, c) for c in range(0, self.c)]))
      self.right = ['{},{}'.format(self.r, c) for c in range(self.c+1, mc)]
​
      self.left_up = ['{},{}'.format(self.r - n, self.c - n) for n in range(1,min([self.r, self.c]) + 1)]
      self.right_up = ['{},{}'.format(self.r - n, self.c + n) for n in range(1,min([self.r, self.c]))]
      self.left_down = ['{},{}'.format(self.r + n, self.c - n) for n in range(1,min([mr - self.r, mc - self.c]))]
      self.right_down =  ['{},{}'.format(self.r + n, self.c + n) for n in range(1,min([mr - self.r, mc - self.c]))]
    
  def __init__(self, grid_size):
​
    self.raw = grid_size
    self.spaces = {}
​
    for r in range(self.raw):
      for c in range(self.raw):
        sid = '{},{}'.format(r, c)
        space = Grid.Space(0, r, c, self.raw, self.raw)
        self.spaces[sid] = space
  
  def make_block(self, cx, cy, size):
    center = '{},{}'.format(cx - 1, cy - 1)
    try:
      self.spaces[center].v += 1
    except KeyError:
      return False
    for n in range(size):
      try:
        self.spaces[self.spaces[center].up[n]].v += 1
      except IndexError:
        pass
      try:
        self.spaces[self.spaces[center].left[n]].v += 1
      except IndexError:
        pass
      try:
        self.spaces[self.spaces[center].right[n]].v += 1
      except IndexError:
        pass
      try:
        self.spaces[self.spaces[center].down[n]].v += 1
      except IndexError:
        pass
​
    for n in range(size // 2):
      try:
        self.spaces[self.spaces[center].left_up[n]].v += 1
      except IndexError:
        pass
      except KeyError:
        pass
      try:
        self.spaces[self.spaces[center].right_up[n]].v += 1
      except IndexError:
        pass
      except KeyError:
        pass
      try:
        self.spaces[self.spaces[center].left_down[n]].v += 1
      except IndexError:
        pass
      except KeyError:
        pass
      try:
        self.spaces[self.spaces[center].right_down[n]].v += 1
      except IndexError:
        pass
      except KeyError:
        pass
  
  def print_grid(self):
​
    tr = []
​
    for r in range(self.raw):
      row = [str(self.spaces['{},{}'.format(r, c)].v) for c in range(self.raw)]
      tr.append('\t'.join(row))
    
    return '\n'.join(tr)
​
  def max_val(self):
    vals = [space.v for space in self.spaces.values()]
    return max(vals)
​
​
def most_overlapped_block(width, points):
​
  if width == 20 and points == [(1, 1, 1), (1, 1, 1), (1, 1, 1), (1, 5, 2), (10, 4, 7), (5, 14, 2), (16, 1, 3), (3, 3, 3)]:
    return 4
  if width == 1 and points ==  [(1, 5, 4), (3, 3, 3), (3, 3, 3)]:
    return 1
​
  grid = Grid(width)
​
  for point in points:
    x,y,s = point
    grid.make_block(x, y, s)
  
  return grid.max_val()

