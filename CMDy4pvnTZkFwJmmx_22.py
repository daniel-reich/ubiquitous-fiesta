
class Sudoku:
  def __init__(self, s):
    self.board = [list(map(int, s[x:x+9])) for x in range(0,81,9)]
  
  def get_row(self, n):
    return self.board[n]
  
  def get_col(self, n):
    return list(list(zip(*self.board))[n])
  
  def get_sqr(self, n, m=-1):
    if m > -1:
      if n in range(3):
        x = 0
      elif n in range(3,6):
        x = 3
      else:
        x = 6
      
      if m in range(3):
        n = x
      elif m in range(3,6):
        n = x +1
      else:
        n = x + 2
​
    if n in range(0,3):
      row = self.board[0:3]
    elif n in range(3,6):
      row = self.board[3:6]
    else:
      row = self.board[6:9]
​
    if n in range(0,7,3):
      return [y for x in row for y in x[0:3]]
    elif n in range(1,8,3):
      return [y for x in row for y in x[3:6]]
    else:
      return [y for x in row for y in x[6:9]]

