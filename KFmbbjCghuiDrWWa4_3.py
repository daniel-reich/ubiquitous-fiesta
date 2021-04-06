
def validate_tic_tac_toe(board):
  xcount = lambda board: str(board).count('X')
  ocount = lambda board: str(board).count('O')
  
  #Rule 1: There must be either an equal amout of Xs and Os or 1 less O than Xs
  
  if ocount(board) not in [xcount(board), xcount(board) - 1]:
    return False
  
  #Rule 2: There cannot be 2 winning conditions:
  
  cols = [''.join([board[r][c] for r in range(3)]) for c in range(3)]
  
  if ('XXX' in board or 'XXX' in cols) and ('OOO' in board or 'OOO' in cols):
    return False
  
  return True

