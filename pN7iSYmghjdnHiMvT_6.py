
# CHARACTER SET
# " " -> empty
# "s" -> ship
# "." -> miss
# "X" -> hit
import numpy as np
class Battleship:
  def __init__(self, scheme, guesses):
    self.scheme = scheme
    self.guesses = guesses
    self.s_board = 0
    self.hitc=0
    self.sunkc=0
  def board(self):
    self.s_board = np.array(list(" ")*25).reshape(5,5)
    Dict_ABC = {'A':0,'B':1,'C':2,'D':3,'E':4}
    for sc in self.scheme:
      x,y =  Dict_ABC[sc[0]] , int(sc[1])-1
      self.s_board[x][y] = 's'
    for gu in self.guesses:
      x,y =  Dict_ABC[gu[0]] , int(gu[1])-1
      if self.s_board[x][y] == 's':
        self.hitc += 1
        self.s_board[x][y] = 'X'
        for a,b in [(a,b) for a in range(5) for b in range(5) if abs(a-x) + abs(b-y) ==1]:
          if self.s_board[a][b] == 'X':
            self.sunkc += 1
            print(self.sunkc)
      else:
        self.s_board[x][y] = '.'
            
    
    return [list(l) for l in self.s_board ]
    
​
  def hits(self):
    return self.hitc
​
  def sunk(self):
    return self.sunkc
​
  def points(self):
    return self.hitc + 2 * self.sunkc

