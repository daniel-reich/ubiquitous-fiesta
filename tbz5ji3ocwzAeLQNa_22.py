
class Maze:
  class Space:
    
    def __init__(self, tpe, row, col, mr, mc):
      self.type = tpe
      self.r = row
      self.c = col
​
      self.above = None
      self.left = None
      self.right = None
      self.below = None
​
      if self.r != 0:
        self.above = '{},{}'.format(self.r - 1, self.c)
      if self.r != mr:
        self.below = '{},{}'.format(self.r + 1, self.c)
      if self.c != 0:
        self.left = '{},{}'.format(self.r, self.c - 1)
      if self.c != mc:
        self.right = '{},{}'.format(self.r, self.c + 1)
      
      if self.type == 0:
        self.safe = True
      else:
        self.safe = False
      
      if self.type == 1:
        self.wall = True
      else:
        self.wall = False
      
      if self.type == 2:
        self.start = True
        self.safe = True
      else:
        self.start = False
      
      if self.type == 3:
        self.end = True
        self.safe = True
      else:
        self.end = False
​
  def __init__(self, grid):
    self.g = grid
​
    self.spaces = {}
​
    for r in range(len(grid)):
      for c in range(len(grid[0])):
        sid = '{},{}'.format(r,c)
        self.spaces[sid] = Maze.Space(grid[r][c], r, c, len(grid) - 1, len(grid[0]) - 1)
​
    self.start = [i for i in self.spaces.values() if i.start == True][0]
    self.end = [i for i in self.spaces.values() if i.end == True]
​
class Person:
​
  def __init__(self, r, c):
    self.r = r
    self.c = c
  
  def move_up(self, maze):
​
    space = maze.spaces['{},{}'.format(self.r, self.c)]
    new_sid = space.above
​
    if new_sid == None:
      return False
    else:
      new_space = maze.spaces[new_sid]
      if new_space.wall == True:
        return False
      else:
        self.r, self.c = [int(i) for i in new_sid.split(',')]
        if new_space.end == True:
          return True
        else:
          return None
  
  def move_down(self, maze):
    
    space = maze.spaces['{},{}'.format(self.r, self.c)]
    new_sid = space.below
​
    if new_sid == None:
      return False
    else:
      new_space = maze.spaces[new_sid]
      if new_space.wall == True:
        return False
      else:
        self.r, self.c = [int(i) for i in new_sid.split(',')]
        if new_space.end == True:
          return True
        else:
          return None
  
  def move_left(self, maze):
    
    space = maze.spaces['{},{}'.format(self.r, self.c)]
    new_sid = space.left
​
    if new_sid == None:
      return False
    else:
      new_space = maze.spaces[new_sid]
      if new_space.wall == True:
        return False
      else:
        self.r, self.c = [int(i) for i in new_sid.split(',')]
        if new_space.end == True:
          return True
        else:
          return None
  
  def move_right(self, maze):
​
    space = maze.spaces['{},{}'.format(self.r, self.c)]
    new_sid = space.right
​
    if new_sid == None:
      return False
    else:
      new_space = maze.spaces[new_sid]
      if new_space.wall == True:
        return False
      else:
        self.r, self.c = [int(i) for i in new_sid.split(',')]
        if new_space.end == True:
          return True
        else:
          return None
  
  def move(self, mve, maze):
​
    if mve == 'N':
      return self.move_up(maze)
    elif mve == 'S':
      return self.move_down(maze)
    elif mve == 'W':
      return self.move_left(maze)
    else:
      return self.move_right(maze) 
​
​
def exit_maze(maze, directions):
​
  maze = Maze(maze)
  person = Person(maze.start.r, maze.start.c)
​
  for direct in directions:
    mv = person.move(direct, maze)
    if mv == False:
      return 'Dead'
    elif mv == True:
      return 'Finish'
  
  return 'Lost'

