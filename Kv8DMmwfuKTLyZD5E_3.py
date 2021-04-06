
def make_dartboard(n):
  board = []
  temp = ''
  for i in range(n):
    for j in range(n):
      temp += str(min(i+1,j+1,n-i,n-j))
    board = board + [int(temp)]
    temp = ''
  return board

