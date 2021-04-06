
def who_won(board):
  # check cross
  if board[0][0] == board[1][1] == board[2][2]:
    return board[0][0]
  elif board[0][2] == board[1][1] == board[2][0]:
    return board[0][2]
  else:
    for i in range(len(board)):
      # check row
      if board[i][0] == board[i][1] == board[i][2]:
        return board[i][0]
      # check column
      elif board[0][i] == board[1][i] == board[2][i]:
        return board[0][i]
    print("Draw")
  return None

