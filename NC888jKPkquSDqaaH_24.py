
def clean_up(files, sort):
  l=[]
  ml=[]
  e=[]
  p=""
  s=""
  c=0
  switch=True
  if sort=="prefix":
    for f in files:
      for x in f:
        if x==".":
          break
        else:
          p=p+x
      if p not in e:
        e.append(p)
        l.append(f)
        ml.append(l)
        l=[]
        p=""
      else:
        for m in ml:
          for d in m:
            for q in d:
              if q==".":
                break
              else:
                s=s+q
            if p==s:
              m.append(f)
              s=""
              p=""
              switch=False
              break
            else: 
              s=""
          if switch==False:
            switch=True
            break
    return ml
  elif sort=="suffix":
    for f in files:
      for x in range(len(f)):
        if f[x]==".":
          p=p+f[x+1:]
      if p not in e:
        e.append(p)
        l.append(f)
        ml.append(l)
        l=[]
        p=""
      else:
        for m in ml:
          for d in m:
            for q in range(len(d)):
              if d[q]==".":
                s=s+d[q+1:]
            if p==s:
              m.append(f)
              s=""
              p=""
              switch=False
              break
            else:
              s=""
          if switch==False:
            switch=True
            break
    return ml

