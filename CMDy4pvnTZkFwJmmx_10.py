
class Sudoku:
  def __init__(self, s):
    self.board = [list(map(int, s))[x:x+9] for x in range (0, 81, 9)]
  
  def get_row(self, n):
    return self.board[n]
    
  def get_col(self, n):
    return [self.board[x][n] for x in range(9)]
    
  def get_sqr(self, n, m = -1):
    if m >= 0: return [self.board[x][y]\
     for x in range (9) if x//3 == n//3\
     for y in range (9) if y//3 == m//3]
    else:
      d={0: (0,0), 1: (0,3), 2: (0,6), 3: (3,0),\
         4: (3,3), 5: (3,6), 6: (6,0), 7: (6,3), 8: (6,6)}
      i, j = d[n]
      return [self.board[x][y] for x in range (9) if x//3 == i//3\
                              for y in range (9) if y//3 == j//3]

