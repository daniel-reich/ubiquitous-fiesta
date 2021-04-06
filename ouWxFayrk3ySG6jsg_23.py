
def who_won(board):
  rows = board[:]
  cols = list(map(list, zip(*board)))
  diag1 = [[board[i][i] for i in range(3)]]
  diag2 = [[board[i][2-i] for i in range(3)]]
  P = rows + cols + diag1 + diag2
  for p in P:
    if len(set(p)) == 1:
      return p[0]

