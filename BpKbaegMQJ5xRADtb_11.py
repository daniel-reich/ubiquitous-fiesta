
def is_unprimeable(num):
  num=str(num)
  l=[]
  u=0
  if num != "1":
    for d in range(2,int(num)):
      if int(num)%d==0:
        u+=1
    if u<1:
      return "Prime Input"
  for i in range(len(num)): 
    for t in range(0,10):
      if i==0:
        e=str(t)+num[i+1:]
      else:
        e=num[:i]+str(t)+num[i+1:]
      e=int(e)
      c=0
      if e==0:
        continue
      for w in range(2,e):
        if e%w==0:
          c+=1
      if c<1:
        l.append(e)
        c=0
        continue
      c=0
  if len(l)==0:
    return "Unprimeable"
  else:
    if 1 in l:
      l.remove(1)
    l.sort()
    return l

