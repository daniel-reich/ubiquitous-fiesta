
class Board:
  class Cup:
​
    def __init__(self, ident, ball = False):
      self.id = ident
      self.ball = ball
    
    def switch(self, other):
      if self.ball == False and other.ball == False:
        return False
      elif other.ball == True:
        self.ball = True
        other.ball = False
        return True
      else:
        self.ball = False
        other.ball = True
        return True
  
  def __init__(self, ball_start_pos):
​
    if ball_start_pos == 'A':
      self.a = Board.Cup('A', True)
    else:
      self.a = Board.Cup('A')
    
    if ball_start_pos == 'B':
      self.b = Board.Cup('B', True)
    else:
      self.b = Board.Cup('B')
    
    if ball_start_pos == 'C':
      self.c = Board.Cup('C', True)
    else:
      self.c = Board.Cup('C')
    
    self.cups = {'A': self.a, 'B': self.b, 'C': self.c}
  
  def interpret(self, string):
​
    c1 = self.cups[string[0]]
    c2 = self.cups[string[1]]
​
    return c1.switch(c2)
  
  def find_ball(self):
    for cup in self.cups.values():
      if cup.ball == True:
        return cup.id
    return False
​
​
def cup_swapping(swaps):
​
  board = Board('B')
​
  for swap in swaps:
    board.interpret(swap)
  
  return board.find_ball()

