
def game_of_life(board):
  row, col = len(board), len(board[0])
  new_board = [['_' for tt in range(col)] for t in range(row)]
  for i in range(row):
    for ii in range(col):
      currState = board[i][ii]
      neighbors = sum([getValOnBoard(board, r, c) 
        for r in range(i-1,i+2)
        for c in range(ii-1,ii+2)
        if (r, c) != (i, ii)
        ])
      if (currState == 0 and neighbors == 3) or (currState == 1 and neighbors in [2, 3]):
        new_board[i][ii] = 'I'
  return '\n'.join([''.join(r) for r in new_board])
​
def getValOnBoard(board, row, col):
  if row < 0 or row >= len(board) or col < 0 or col >= len(board[0]):
    return 0
  else: 
    return board[row][col]

