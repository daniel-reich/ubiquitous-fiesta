
def game_of_life(board):
  result = [[] for x in board]
  poss = [(1,1), (0,1), (1,0), (-1,1), (1,-1), (-1,-1), (0,-1), (-1,0)]
  for i in range(len(board)):
    for j in range(len(board[i])):
      empty, filled = 0, 0
      for k in poss:
        if i+k[0] >= 0 and i+k[0] < len(board) and j+k[1] >=0 and j+k[1] < len(board[0]):
          if board[i+k[0]][j+k[1]] == 1: filled +=1 
          else: empty += 1
      if board[i][j] == 0 and filled == 3: result[i].append("I")
      elif board[i][j] == 1 and (filled == 2 or filled == 3): result[i].append("I")
      else: result[i].append("_")
  return "\n".join(["".join(x) for x in result])

