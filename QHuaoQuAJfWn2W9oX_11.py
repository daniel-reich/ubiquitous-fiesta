
def check_board(col, row):
  d = {'h':7,'g':6,'f':5,'e':4,'d':3,'c':2,'b':1,'a':0}
  w,h=8,8
  Matrix = [[0 for x in range(w)] for y in range(h)]
  for i in range (8):
    Matrix[8-row][i]=1
    Matrix[i][d[col]]=1
  for i in range (8-row,8):
    for j in range (8):
      if(abs(j-d[col])==abs(i-(8-row))):
        Matrix[i][j]=1
  
  for i in range (8-row,-1,-1):
    for j in range (8):
      if(abs(j-d[col])==abs(i-(8-row))):
        Matrix[i][j]=1
  Matrix[8-row][d[col]]=0
  return Matrix

