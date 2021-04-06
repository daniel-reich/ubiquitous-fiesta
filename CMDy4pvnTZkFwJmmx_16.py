
class Sudoku:
  def __init__(self, txt):
    meh = [int(d) for d in txt]
    self.board = [meh[9*n:9*n+9] for n in range(9)]
  
  def get_row(self, n):
    return self.board[n]
  
  def get_col(self, n):
    return [row[n] for row in self.board]
    
  def get_sqr(self, n, m=None):
    if m!=None:
      n = 3*(n//3)+m//3
    return sum((self.board[3*(n//3)+i][3*(n%3):3*(n%3)+3] for i in range(3)),[])

