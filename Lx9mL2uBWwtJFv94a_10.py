
def checker_board(n, el1, el2):
  board=[]
  for i in range(n):
    board.append([el1]*n)
  
  if el1==el2:
    return "invalid"
  else:
    for row in range(n):
      for column in range(n):
        if (row+column)%2==1:
          board[row][column]=el2
    return board

