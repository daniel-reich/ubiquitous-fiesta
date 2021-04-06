
def bingo_check(board):
  z=len(board)
  e=len(board[0])
  c=0
  x=0
  l=0
  for i in range(e):  
    for t in range(z):
      if board[t][i]=="x":
        c+=1
    if c==z:
      return True
    c=0
  for i in range(z):
    for t in range(e):
      if board[i][t]=="x":
        c+=1
    if c==e:
      return True
    c=0
  for i in range(e):
    if board[x][l] == "x":
      c+=1
    x+=1
    l+=1
  if c==5:
    return True
  c=0
  x=0
  l=4
  for i in range(e):
    if board[x][l]=="x":
      c+=1
    x+=1
    l-=1
  if c==5:
    return True
  else:
    return False

