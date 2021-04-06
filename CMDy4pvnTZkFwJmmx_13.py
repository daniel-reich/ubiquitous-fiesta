
class Sudoku:
  def __init__(self, s):
    self.board = []
    for i in range(0, 81, 9):
      self.board.append([int(c) for c in s[i:i+9]])
  
  def get_row(self, n):
    return self.board[n]
    
  def get_col(self, n):
    return [row[n] for row in self.board]
    
  def get_sqr(self, n, m=None):
    sqr = []
    
    if m is None:
      yx_from_n = [
        (0, 0), (0, 3), (0, 6),
        (3, 0), (3, 3), (3, 6),
        (6, 0), (6, 3), (6, 6),
      ]
      y, x = yx_from_n[n]
    else:
      y, x = n // 3 * 3, m // 3 * 3
​
    for i in range(y, y+3):
      for j in range(x, x+3):
        sqr.append(self.board[i][j])
        
    return sqr

