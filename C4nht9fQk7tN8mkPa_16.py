
def cannot_capture(board):
  checks = []
  def check_capture(x, y, board, line):
    if x >= 0 and x < len(board) and y >= 0 and y < len(line):
      return board[x][y]
  for i, line in enumerate(board):
    for j, cell in enumerate(line):
      if cell == 1:
        checks.append(check_capture(i+2, j+1, board, line))
        checks.append(check_capture(i+2, j-1, board, line))
        checks.append(check_capture(i-2, j+1, board, line))
        checks.append(check_capture(i-2, j-1, board, line))
        checks.append(check_capture(i+1, j+2, board, line))
        checks.append(check_capture(i+1, j-2, board, line))
        checks.append(check_capture(i-1, j+2, board, line))
        checks.append(check_capture(i-1, j-2, board, line))
  if 1 in checks:
    return False
  else:
    return True

