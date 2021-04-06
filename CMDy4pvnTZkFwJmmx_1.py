
import re
​
class Sudoku:
  def __init__(self, txt):
    self.board = [list(map(int, i)) for i in re.findall('\d{9}', txt)]
    
  def get_row(self, n):
    return self.board[n]
    
  def get_col(self, n):
    return [self.board[i][n] for i in range(9)]
    
  def get_sqr(self, n, m=None):
    if m is not None: n = n//3*3 + m//3
    return [self.board[r][c] for r in range(n//3*3, n//3*3+3) for c in range(n%3*3, n%3*3+3)]

