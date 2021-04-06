
def tic_tac_toe(board):
  k=['O','X']
  y=[]
  for i in board:
    for j in i:
      y.append(j)
  s=[[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
  for l in k:
    for i in s:
      t=0
      for j in i:
        if(y[j]==l):
          t+=1
      if(t==3):
        return l
  return 'Draw'

