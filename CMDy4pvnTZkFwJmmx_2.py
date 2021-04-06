
class Sudoku:
  def __init__(self, board):
    self.board = [list(map(int,board[i:i+9])) for i in range(0,81,9)]
​
  def get_row(self, n):
    return self.board[n]
​
  def get_col(self, n):
    return [self.board[i][n] for i in range(9)]
​
  def get_sqr(self,n,m=None):
    if m is None:
      i = (n//3)*3
      j = (n%3)*3
    else:
      i = n - n%3
      j = m - m%3
    
    return [self.board[i+y][j+x] for y in range(3) for x in range(3)]

