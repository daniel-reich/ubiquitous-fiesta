
class Sudoku:
  def __init__(self, s):
    self.s = s
    self.board = []
    idxs = [0, 9]
    for i in range(9):
      self.board.append([int(i) for i in s[idxs[0]:idxs[1]]])
      idxs[0] += 9
      idxs[1] += 9
    # ^^slicing original string to create the matrix
  
  def get_row(self, n):
    return self.board[n]
  
  def get_col(self, n):
    return [i[n] for i in self.board]
  
  def get_sqr(self, n, m=None):
    my_dict = {0:0, 1:0, 2:0, 3:1, 4:1, 5:1, 6:2, 7:2, 8:2}
    squares = []
    board = self.board
    for row_idx in range(0, len(board), 3):
      squares.append(board[row_idx][:3] + board[row_idx + 1][:3] + board[row_idx + 2][:3])
      squares.append(board[row_idx][3:6] + board[row_idx + 1][3:6] + board[row_idx + 2][3:6])
      squares.append(board[row_idx][6:] + board[row_idx + 1][6:] + board[row_idx + 2][6:])
    if m is None:
      return squares[n]
    squares = [squares[:3], squares[3:6], squares[6:]]
    return squares[my_dict[n]][my_dict[m]]

