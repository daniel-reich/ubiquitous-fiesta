
def final(r, c, i):
  board = [[0 for j in range(0,c)] for k in range(0,r)]
  for entry in i:
    for k in range(0,r):
      for j in range(0,c):
        if entry[1] == "r" and k == int(entry[0]):
          board[k][j] += 1
        elif entry[1] == "c" and j == int(entry[0]):
          board[k][j] += 1
  return board

