
import re
class Sudoku:                       # Sudoku Parser
  def __init__(self, string):
    self.board = [[int(n) for n in i] for i in [list(x) for x in re.findall(r"(\d{9})", string)]]
    self.board_t = [list(x) for x in list(zip(*self.board))]
​
  def get_row(self, n):
    return self.board[n]
  def get_col(self, n):
    return self.board_t[n]
  def get_sqr(self, n, *m):
    squares = []
    for i in range(0, 9, 3):
      for j in range(0,9, 3):
        results = self.board[i][j:j+3] + self.board[i+1][j:j+3] + self.board[i+2][j:j+3]
        squares.append(results)
    if not m: return squares[n]
    m = m[0]
    return (squares[0] if m<3 else squares[1] if m<6 else squares[2]) if n<3 else (squares[3] if m<3 else squares[4] if m<6 else squares[5]) if n<6 else (squares[6] if m<3 else squares[7] if m<6 else squares[8])

