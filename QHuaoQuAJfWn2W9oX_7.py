
def check_board(col, row):
  move=xmove(col,row)+pmove(col,row)
  return [[[i,j] in move for i in range(1,9)] for j in range(1,9)][::-1]
​
def sub(a,b,x,y):
  memx,memy,res=x,y,[]
  c1='ord(a)+x<=104' if x>0 else '97<=ord(a)+x'
  c2='b+y<=8' if y>0 else '1<=b+y'
  while eval(c1) and eval(c2):
    res+=[[ord(a)-96+x,b+y]]
    x+=memx;y+=memy
  return res
​
def xmove(a,b):
  return sub(a,b,-1,1)+sub(a,b,-1,-1)+sub(a,b,1,1)+sub(a,b,1,-1)
​
def pmove(a,b):
  return sub(a,b,-1,0)+sub(a,b,1,0)+sub(a,b,0,1)+sub(a,b,0,-1)

