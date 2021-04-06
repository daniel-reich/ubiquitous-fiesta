
class Sudoku:
  def __init__(self,string):
    self.board = []
    for i in range(0,9):
      self.board.append([int(string[j]) for j in range(9*i,9*i + 9)])
  def get_row(self,n):
    return self.board[n]
  def get_col(self,n):
    return [self.board[i][n] for i in range(0,9)]
  def get_sqr(self,*n):
    if len(n) == 2:
      s = 3*(n[0] // 3) + n[1] // 3
    else:
      s = n[0]
    r = 3 * (s // 3)
    c = 3 * (s % 3)
    lst = []
    for i in range(r,r+3):
      lst.extend([self.board[i][j] for j in range(c,c+3)])
    return lst

