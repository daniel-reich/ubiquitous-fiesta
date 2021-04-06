
def tic_tac_toe(board):
  rows = board
  cols = list(map(list, zip(*board)))
  diag1 = [[board[i][i] for i in range(3)]]
  diag2 = [[board[i][-i-1] for i in range(3)]]
  
  combs = rows + cols + diag1 + diag2
  if ['X', 'X', 'X'] in combs:
    return 'Player 1 wins'
  elif ['O', 'O', 'O'] in combs:
    return 'Player 2 wins'
  else:
    return "It's a Tie"

