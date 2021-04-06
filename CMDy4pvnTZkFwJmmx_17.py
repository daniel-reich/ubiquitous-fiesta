
class Sudoku:
  def __init__(self, board):
    self.board = [[int(board[r*9+c]) for c in range(9)] for r in range(9)]
  def get_row(self, n):
    return self.board[n]
  def get_col(self, n):
    return [row[n] for row in self.board]
  def get_sqr(self, n, m=None):
    if m == None:
      r, c = (n//3)*3, (n%3)*3
    else:
      r, c = (n//3)*3, (m//3)*3
    return [self.board[r][c], self.board[r][c+1], self.board[r][c+2],
            self.board[r+1][c], self.board[r+1][c+1], self.board[r+1][c+2],
            self.board[r+2][c], self.board[r+2][c+1], self.board[r+2][c+2]]

