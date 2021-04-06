
class Grid:
  class Space:
​
    def __init__(self, r, c, mr, mc, bomb_typ = '0'):
      self.r = r
      self.c = c
      self.bt = bomb_typ
​
      self.left_near = None
      self.left_up = None
      self.left_down = None
​
      self.up = None
      self.down = None
​
      self.right_near = None
      self.right_up = None
      self.right_down = None
​
      if self.c != 0:
        self.left_near = '{},{}'.format(self.r, self.c-1)
        if self.r != 0:
          self.left_up = '{},{}'.format(self.r - 1, self.c - 1)
        if self.r != mr:
          self.left_down = '{},{}'.format(self.r + 1, self.c - 1)
      
      if self.c != mc:
        self.right_near = '{},{}'.format(self.r, self.c + 1)
        if self.r != 0:
          self.right_up = '{},{}'.format(self.r - 1, self.c + 1)
        if self.r != mr:
          self.right_down = '{},{}'.format(self.r + 1, self.c + 1)
      
      if self.r != 0:
        self.up = '{},{}'.format(self.r - 1, self.c)
      if self.r != mr:
        self.down = '{},{}'.format(self.r + 1, self.c)
​
      self.plus_places = [self.up, self.down, self.left_near, self.right_near]
      self.x_places = [self.left_up, self.left_down, self.right_up, self.right_down]
​
      if self.bt in ['+', 'x']:
        self.ignited = False
      else:
        self.ignited = None
    
    def explode(self, spaces):
      if self.ignited == None:
        return False
      elif self.ignited == True:
        return None
      else:
        self.ignited = True
        if self.bt == '+':
          for sid in self.plus_places:
            if sid == None:
              continue
            space = spaces[sid]
            if space.ignited == False:
              space.explode(spaces)
        elif self.bt == 'x':
          for sid in self.x_places:
            if sid == None:
              continue
            space = spaces[sid]
            if space.ignited == False:
              space.explode(spaces)
        return True
  
  def __init__(self, grid):
​
    self.raw = grid
    self.spaces = {}
    self.bombs = []
    self.exploded = []
​
    for r in range(len(grid)):
      for c in range(len(grid[0])):
        sid = '{},{}'.format(r, c)
        space = Grid.Space(r, c, len(grid) - 1, len(grid[0]) - 1, grid[r][c])
        self.spaces[sid] = space
​
        if space.bt in ['+', 'x']:
          self.bombs.append(sid)
​
  def explode_bomb(self, bomb_index):
​
    bomb = self.spaces[self.bombs[bomb_index]]
    t = bomb.explode(self.spaces)
​
    if t != True:
      return False
​
    for bob in self.bombs:
      if self.spaces[bob].ignited == True and bob not in self.exploded:
        self.exploded.append(bob)
    
    return True
​
​
def min_bombs_needed(grid):
​
  grid = Grid(grid)
​
  n = 0
  c = 0
​
  while len(grid.exploded) < len(grid.bombs):
    t = grid.explode_bomb(n)
    n += 1
    if t == True:
      c += 1
  
  return c

