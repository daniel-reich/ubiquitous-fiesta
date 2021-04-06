
def divide(x,y,s=0):
  if s==0: return divide(abs(x),abs(y),[1,-1][(x<0)^(y<0)])
  return 0 if x<y else s + divide(x-y,y,s)

