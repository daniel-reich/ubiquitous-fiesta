
def modulo(x,y,s=1):
  if x<0:s=-1
  if y<0 and x>0:s=1
  x=abs(x)
  y=abs(y)
  if x==y:return 0
  elif y<x:return modulo(x-y,y,s)
  else:return x*s

