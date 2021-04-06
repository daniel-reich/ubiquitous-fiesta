
from copy import deepcopy
class Move:
  dirn = {'up': (-1, 0), 'down': (1, 0), 'left': (0, -1), 'right': (0, 1)}
  
  def __init__(self, mat):
    self.height = len(mat)
    self.width = len(mat[0])
    for r, c in [(r,c) for r in range(self.height) for c in range(self.width)]:
      if mat[r][c] == 1:
        break
    self.r, self.c, self.mat = r, c, deepcopy(mat)
​
  def make_move(self, m):
    if m == 'stop':
      return self.mat
    if m in self.dirn:
      self.set_pos(self.r, self.c, 0)
      dr, dc = self.dirn[m]
      self.r = (self.r + self.height + dr) % self.height
      self.c = (self.c + self.width + dc) % self.width
      self.set_pos(self.r, self.c, 1)
      return self.make_move
​
  def set_pos(self, r, c, v):
    self.mat[r][c] = v
​
def move(mat):
  return Move(mat).make_move

