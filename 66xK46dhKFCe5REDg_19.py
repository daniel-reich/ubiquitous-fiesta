
def x_and_o(board):
  board = [l.split("|") for l in board]
  for r in range(3):
    for c in range(3):
      if board[r][c] == " ":
        tests = [all(board[r][i] == "X" for i in range(3) if i != c), 
                all(board[i][c] == "X" for i in range(3) if i != r),
                r == c  and all(board[i][i] == "X" for i in range(3) if i != c),
                r == 2 - c and all(board[2-i][i] == "X" for i in range(3) if i != c)]
        if any(tests):
          return [r +1, c+ 1]
  return False

