
def simplify(txt):
  y=int(txt[txt.index('/')+1:])
  x=int(txt[:txt.index('/')])
  if x%y==0:
    return str(int(x/y))
  else:   
    z=min(x,y)+1
    for i in range(min(x,y)):
      z=z-1
      if x%z==0 and y%z==0:
        break
  return str(int(x/z))+'/'+str(int(y/z))

