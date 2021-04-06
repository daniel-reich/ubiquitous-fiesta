
def asteroid_collision(asteroids):
  new=asteroids.copy()
​
  x=new.pop(0)
  out=[]
​
  while True:
    old=0
    if len(out)>0:old=out.pop()
    if  old >0 and x <0: # different sign
      if abs(old)==abs(x):x,old=0,0
      if abs(old)>abs(x):x=old
    else:
      if old!=0: out.append(old)
      if x!=0: out.append(x)
      if len(new)==0: return out
      x=new.pop(0)

