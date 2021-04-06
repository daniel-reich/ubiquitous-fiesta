
def lemonade(bills):
  f,t=0,0
  for b in bills:
    if b==5:
      f+=1
    elif b==10:
      if not f:
        return False
      f-=1
      t+=1
    else:
      if not f or (f<3 and not t):
        return False
      elif t>1:
        t-=1
        f-=1
      else:
        f-=3
  return True

