
def game_of_life(board):
  x = [(-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1)]
  new = ''
  for row in range(len(board)):
    for i in range(len(board[row])):
      n = 0
      for j in x:
        try:
          if j[0] + row >= 0 and j[1] + i >= 0:
            n += board[j[0] + row][j[1] + i]
        except IndexError:
          pass
      if board[row][i] == 1:
        if n <= 1 or n >= 4:
          new += '_'
        else:
          new += 'I'
      else:
        if n == 3:
          new += 'I'
        else:
          new += '_'
    new += '\n'
  if True: #board == [[0, 0, 0], [0, 1, 0], [0, 0, 0]]:
    return new.rstrip()
  return board

