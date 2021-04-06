
def drange(*args):
  f=[]
  w=[]
  if len(args)==1:
    for i in range(0,args[0]):
      f.append(i)
    return tuple(f)
  elif len(args)==2:
    for i in range(args[0],args[1]):
      f.append(i)
    return tuple(f)
  else:
    c=0
    s=0
    switch=False
    for d in args:
      d=str(d)
      for x in d:
        if switch==True:
          c+=1
        if x==".":
          switch=True
      if c>s:
        s=c
      c=0
      switch=False
    z=0
    while(True):
      if z==0:
        z=args[0]
      else:
        z=round(z+args[2],s)
      if z>=args[1]:
        w=tuple(w)
        return w
      else:
        w.append(z)

