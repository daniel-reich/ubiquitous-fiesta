
def bingo_check(board):
  diag1 = []
  diag2 = []
  for i in range(len(board)):
    row = board[i]
    col = [b[i] for b in board]
    if len(set(row)) == 1 or len(set(col)) == 1: return True
    diag1.append(board[i][i])
    diag2.append(board[i][-i - 1])
  if len(set(diag1)) == 1 or len(set(diag2)) == 1: return True
  return False

