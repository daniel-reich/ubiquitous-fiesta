
def tic_tac_toe(board):
  r1 = board[0]
  r2 = board[1]
  r3 = board[2]
  c1 = [board[0][0], board[1][0], board[2][0] ]
  c2 = [board[0][1], board[1][1], board[2][1] ]
  c3 = [board[0][2], board[1][2], board[2][2] ]
  d1 = [board[0][0], board[1][1], board[2][2]]
  d2 = [board[0][2], board[1][1], board[2][0]]
  all_poss = [r1,r2,r3,c1,c2,c3,d1,d2]
  for a in all_poss:
    if a.count('X') == 3:
      return 'X'
    elif a.count('O') == 3:
      return 'O'
  return "Draw"

