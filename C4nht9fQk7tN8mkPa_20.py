
def cannot_capture(board):
  capture_positions = ((-2, 1), (-1, 2), (-1, -2), (2, 1), 
             (2, -1), (1, -2), (-2, -1), (1, 2))
  
  for i in range(8):
    for j in range(8):
      if board[i][j] == 1:
        for r, c in capture_positions:
          if 0 <= i+r <= 7 and 0 <= j+c <= 7 and board[i+r][j+c] == 1:
            return False
  return True

