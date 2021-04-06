
class Sudoku:
  def __init__(self, x):
    self.board = [[int(x[i+9*j]) for i in range(9)] for j in range(9)]
​
  def get_row(self, n):
    return self.board[n]
​
  def get_col(self, n):
    return [self.board[i][n] for i in range(9)]
​
  def get_sqr(self, *n):
    if len(n) != 1:
      n = [3*(n[0]//3) + n[1]//3]
    return [self.board[x//3 + 3*(n[0]//3)][(x%3 + n[0]*3) %9] for x in range(9)]

