
class Battleship:
  values = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4}
​
  def __init__(self, scheme, guesses):
    self.scheme = scheme
    self.guesses = guesses
​
  def board(self):
    board = [[' ']*5 for i in range(5)]
    for spot in self.scheme:
      board[self.values[spot[0]]][int(spot[1]) -1] = 's'
    for spot in self.guesses:
      if spot in self.scheme:
        board[self.values[spot[0]]][int(spot[1]) -1] = 'X'
      else:
        board[self.values[spot[0]]][int(spot[1]) -1] = '.'
    return board
​
  def hits(self):
    return sum(g in self.scheme for g in self.guesses)
​
  def sunk(self):
    b = self.board()
    sunk = 0
    for i in range(5):
      for j in range(1, 5):
        if b[i][j] == 'X' and b[i][j-1] == 'X':
          sunk += 1
    for i in range(1, 5):
      for j in range(5):
        if b[i-1][j] == 'X' and b[i][j] == 'X':
          sunk += 1
    return sunk
    
  def points(self):
    return self.hits() + self.sunk() * 2

