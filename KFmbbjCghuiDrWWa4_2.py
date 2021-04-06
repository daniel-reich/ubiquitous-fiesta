
def validate_tic_tac_toe(board):
  rows = ",".join(board)
  cols = ",".join(["".join(board[r][c] for r in range(3)) for c in range(3)])
  diags = "".join([board[i][i] for i in range(3)]) + "," + "".join([board[2-i][i] for i in range(3)])
  if not 0<=rows.count('X')-rows.count('O')<=1:
    return False
  lines = rows + "," + cols + "," + diags
  cX, cO = lines.count("XXX"), lines.count("OOO")
  if cX and cO:
    return False
  return True

