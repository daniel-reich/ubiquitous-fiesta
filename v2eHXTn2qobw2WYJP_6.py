
def minesweeper_numbers(board):
  for i in range(len(board)):
    for j in range(len(board[i])):
      if board[i][j] == 1:
        board[i][j] = 9
        
  for i in range(len(board)):
    for j in range(len(board[i])):
      count = 0
      if board[i][j] != 9:
        rightSide = j+1 < len(board[i])
        leftSide = j-1 >= 0
        topSide = i-1 >= 0
        bottomSide = i+1 < len(board)
        if rightSide:
          if board[i][j+1] == 9:
            count += 1
        if leftSide:
          if board[i][j-1] == 9:
            count += 1
        if topSide:
          if board[i-1][j] == 9:
            count += 1
        if bottomSide:
          if board[i+1][j] == 9:
            count += 1
        if topSide and rightSide:
          if board[i-1][j+1] == 9:
            count += 1
        if topSide and leftSide:
          if board[i-1][j-1] == 9:
            count += 1
        if bottomSide and rightSide:
          if board[i+1][j+1] == 9:
            count += 1
        if bottomSide and leftSide:
          if board[i+1][j-1] == 9:
            count += 1
        board[i][j] = count
  return board

