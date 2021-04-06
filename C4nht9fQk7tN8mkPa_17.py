
def cannot_capture(board):
  
  def istile(y, x):
    return 0 <= y <= 7 and 0 <= x <= 7
  
  def moves(y, x):
    lst = [(y-2, x-1), (y-2, x+1),
           (y-1, x-2), (y-1, x+2),
           (y+1, x-2), (y+1, x+2),
           (y+2, x-1), (y+2, x+1)]
    
    return [pos for pos in lst if istile(pos[0], pos[1])]
    
  for y, row in enumerate(board):
    for x, isknight in enumerate(row):
      if isknight:
        for legal_move in moves(y, x):
          if board[legal_move[0]][legal_move[1]]: return False
            
  return True

