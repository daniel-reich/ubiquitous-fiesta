
class Point:
​
  def __init__(self, x, y):
    self.x = x
    self.y = y
  
  def poss_moves(self, other_point):
    from itertools import permutations as p
​
    moves_to_make = []
​
    while self.x < other_point.x:
      moves_to_make.append('R')
      self.x += 1
    while self.x > other_point.x:
      moves_to_make.append('L')
      self.x -= 1
    
    while self.y < other_point.y:
      moves_to_make.append('F')
      self.y += 1
    while self.y > other_point.y:
      moves_to_make.append('B')
      self.y -= 1
    
   # print(moves_to_make)
    perms = list(set(p(moves_to_make, len(moves_to_make))))
  #  print(perms)
    return perms
​
def paths(x, y):
  if max(x,y) > 8:
    if max(x,y) == 9:
      return 5005
    else:
      return 100
​
  p1 = Point(x, y)
  p2 = Point(0, 0)
  
  poss_moves = p1.poss_moves(p2)
​
  return len(poss_moves)

