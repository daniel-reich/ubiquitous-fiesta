
class Sudoku:
  def __init__(self, board):
    self.board = [[int(board[9*n + i]) for i in range(9)] for n in range(9)]
    self.columns = [[int(board[n + 9*i]) for i in range(9)] for n in range(9)]
  def get_row(self, n):
    return self.board[n]
  def get_col(self, n):
    return self.columns[n]
  def get_sqr(self, n, *m):
    if m:
      m = m[0]
      n = 3 * (n // 3) + (m // 3)
    squ = self.get_row(3*(n // 3))[(n % 3)*3:(n % 3)*3+3]
    squ.extend(self.get_row(3*(n // 3) + 1)[(n % 3)*3:(n % 3)*3+3])
    squ.extend(self.get_row(3*(n // 3) + 2)[(n % 3)*3:(n % 3)*3+3])
    return squ

