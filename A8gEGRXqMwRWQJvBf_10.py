
def tic_tac_toe(board):
  primary_diag = []
  secondary_diag = []
  horizontal = []
  vertical_0 = []
  vertical_1 = []
  vertical_2 = []
  
  for i in range(3):
    primary_diag.append(board[i][i])
    secondary_diag.append(board[i][-i - 1])
    horizontal.append("".join(board[i]))
    vertical_0.append(board[i][0])
    vertical_1.append(board[i][1])
    vertical_2.append(board[i][2])
  
  primary_diag = ["".join(primary_diag)]
  secondary_diag = ["".join(secondary_diag)]
  vertical_0 = ["".join(vertical_0)]
  vertical_1 = ["".join(vertical_1)]
  vertical_2 = ["".join(vertical_2)]
​
  lines = primary_diag + secondary_diag + horizontal + vertical_0 + vertical_1 + vertical_2
  
  if "XXX" in lines:
    return "X"
  elif "OOO" in lines:
    return "O"
  else:
    return "Draw"

