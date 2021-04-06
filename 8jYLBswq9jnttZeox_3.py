
class Grid:
  class Space:
​
    def __init__(self, white, row, col):
      self.w = white
      self.r = row
      self.c = col
    
    def flip(self):
      if self.w == 1:
        self.w = 0
      else:
        self.w = 1
      return True
  
  def __init__(self, grid):
    self.grid = grid
    self.spaces = {}
​
    for r in range(len(grid)):
      for c in range(len(grid[0])):
        self.spaces['{},{}'.format(r,c)] = Grid.Space(grid[r][c], r, c)
    
    self.min_row = 0
    self.min_col = 0
​
    self.max_row = len(grid) - 1
    self.max_col = len(grid[0]) - 1
  
  def expand_up(self):
​
    self.min_row -= 1
​
    for c in range(self.min_col, self.max_col + 1):
      self.spaces['{},{}'.format(self.min_row, c)] = Grid.Space(0, self.min_row, c)
    
    return True
  
  def expand_down(self):
    self.max_row += 1
​
    for c in range(self.min_col, self.max_col + 1):
      self.spaces['{},{}'.format(self.max_row, c)] = Grid.Space(0, self.max_row, c)
    
    return True
  
  def expand_left(self):
    self.min_col -= 1
​
    for r in range(self.min_row, self.max_row + 1):
      self.spaces['{},{}'.format(r, self.min_col)] = Grid.Space(0, r, self.min_col)
    
    return True
  
  def expand_right(self):
    self.max_col += 1
​
    for r in range(self.min_row, self.max_row + 1):
      self.spaces['{},{}'.format(r, self.max_col)] = Grid.Space(0, r, self.max_col)
    
    return True
​
  def display(self):
    tr = []
​
    for r in range(self.min_row, self.max_row + 1):
      row = []
      for c in range(self.min_col, self.max_col + 1):
        space = self.spaces['{},{}'.format(r,c)]
        row.append(str(space.w))
        #print(r,c)
      tr.append('\t'.join(row))
    
    print('\n'.join(tr))
    return [[int(i) for i in j.split('\t')] for j in tr]
​
class Ant:
​
  def __init__(self, row, col, direct):
    self.r = row
    self.c = col
    self.d = direct
  
  def move_east(self, grid):
    if grid.max_col > self.c:
      self.c += 1
      return True
    else:
      grid.expand_right()
      self.c += 1
      return True
    return False
  
  def move_west(self, grid):
    if grid.min_col < self.c:
      self.c -= 1
      return True
    else:
      grid.expand_left()
      self.c -= 1
      return True
    return False
  
  def move_north(self, grid):
    if grid.min_row < self.r:
      self.r -= 1
      return True
    else:
      grid.expand_up()
      self.r -= 1
      return True
    return False
  
  def move_south(self, grid):
    if grid.max_row > self.r:
      self.r += 1
      return True
    else:
      grid.expand_down()
      self.r += 1
      return True
    return False
  
  def move(self, grid):
​
    current_space_id = '{},{}'.format(self.r, self.c)
    current_space = grid.spaces[current_space_id]
​
    if current_space.w == 1:
      self.d += 1
      while self.d >= 4:
        self.d -= 4
    else:
      self.d -= 1
      while self.d < 0:
        self.d += 4
    
    current_space.flip()
​
    if self.d == 0:
      return self.move_north(grid)
    elif self.d == 1:
      return self.move_east(grid)
    elif self.d == 2:
      return self.move_south(grid)
    elif self.d == 3:
      return self.move_west(grid)
    else:
      print('ERROR!!! >>UNKNOWN DIRECTION: {}<<'.format(self.d))
      return False
​
def langtons_ant(grid, column, row, n, direction=0):
  
  grid = Grid(grid)
  ant = Ant(row, column, direction)
​
  for iteration in range(n):
    ant.move(grid)
  
  return grid.display()

