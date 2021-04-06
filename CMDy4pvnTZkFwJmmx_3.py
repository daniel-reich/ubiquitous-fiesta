
class Sudoku:
  board = ''
  def __init__(self,board):
    self.board = [list(map(int,board[i:i+9])) for i in range(0,81,9)]
  def get_row(self,n):
    return self.board[n]
  def get_col(self,n):
    return [self.board[i][n] for i in range(9)]
  def get_sqr(self,*args):
    if len(args)==1:
      return [self.board[i][j] for i in range((args[0]//3)*3,((args[0]//3)*3)+3) for j in range((args[0]%3)*3,((args[0]%3)*3)+3)]
    else:
      return [self.board[i][j] for i in range((args[0]//3)*3,((args[0]//3)*3)+3) for j in range((args[1]//3)*3,((args[1]//3)*3)+3)]

