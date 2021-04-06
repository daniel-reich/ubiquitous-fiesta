
def game_of_life(board):
  answer = []
  for y in range(len(board)):
    row = []
    for x in range(len(board[y])):
      count = 0
      if (y-1) > -1 and (x -1) > -1 and board[y -1][x - 1] == 1:
          count += 1
      if (y-1) > -1 and board[ y -1][x] == 1:
          count +=1
      if (y -1) > -1 and (x + 1) < len(board[y - 1]) and board[y - 1][ x + 1] == 1:
          count += 1
      if ( x - 1 ) > -1 and board[y][x -1] == 1:
          count += 1
      if board[y][x] == 1:
          count += 1
      if (x + 1) < len(board[y - 1]) and board[y][x + 1] == 1:
          count += 1
      if ( y + 1 ) < len(board) and (x -1 ) > -1 and board[ y +1][x - 1] == 1:
          count += 1
      if ( y + 1 ) < len(board) and board[y + 1][x] == 1:
          count +=1
      if  (y + 1 ) < len(board) and (x + 1) < len(board[y - 1]) and board[y + 1][x + 1] == 1:
          count +=1
      if count < 3 or count > 4 or (count == 4 and board[y][x] == 0):
        row.append("_")
      else:
        row.append("I")
    answer.append(''.join(row) + "\n")
    row.clear()
  return ''.join(answer)[:-1]

