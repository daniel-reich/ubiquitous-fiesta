
# CHARACTER SET
# " " -> empty
# "s" -> ship
# "." -> miss
# "X" -> hit
​
class Battleship:
  def __init__(self, scheme, guesses):
    self.scheme = scheme
    self.guesses = guesses
    self.game = [[' ']*5 for i in range(5)]
    self.hit = 0
    self.cruisers = 0
​
    
  def board(self):
    xaxis = 'ABCDE'
    for i in self.scheme:
      x,y = xaxis.find(i[0]),int(i[1])-1
      self.game[x][y] = 's'
    for i in self.guesses:
      x,y = xaxis.find(i[0]),int(i[1])-1
      if self.game[x][y] == 's':
        self.game[x][y] = 'X'
      else:
        self.game[x][y] = '.'
    return self.game
​
  def hits(self):
    self.hit += sum(i.count('X') for i in self.game)
    return self.hit
​
  def sunk(self):
    for i in range(5):
      for j in range(5):
        up = self.game[i-1][j] if i!=0 else ' '
        left = self.game[i][j-1] if j!=0 else ' '
        if self.game[i][j]=='X' and 'X' in (up,left):
          self.cruisers+=1
    return self.cruisers
​
  def points(self):
    return self.hit+self.cruisers*2

