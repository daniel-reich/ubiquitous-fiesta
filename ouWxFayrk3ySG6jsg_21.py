
def who_won(board):
  rows = ["".join(a) for a in board]
  cols = [a[i] for i in range(3) for a in board]
  cols = ["".join(cols[i: i + 3]) for i in [0, 3, 6]]
  dia1 = board[0][0] + board[1][1] + board[2][2]
  dia2 = board[0][2] + board[1][1] + board[2][0]
  patterns = rows + cols + [dia1, dia2]
  return 'X' if 'XXX' in patterns else 'O'

