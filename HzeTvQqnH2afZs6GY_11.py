
def generate_rug(n, direction):
  if direction=="left":
    l=[]
    e=[]
    ml=[]
    switch=True
    for i in range(n):
      l.append(i)
    ml.append(l)
    while(True):
      if len(e)>0:
        ml.append(e)
        switch=True
        l=list(e)
        e=[]
      if len(ml)==n:
        return ml
      for r in l:
        if r==0:
          switch=False
          e.append(r+1)
        else:
          if switch==False:
            e.append(r-1)
          else:
            e.append(r+1)
  if direction=="right":
    l=[]
    e=[]
    ml=[]
    switch=True
    for i in range(n):
      l.append(i)
    l.sort(reverse=True)
    ml.append(l)
    while(True):
      if len(e)>0:
        ml.append(e)
        switch=True
        l=list(e)
        e=[]
      if len(ml)==n:
        return ml
      for r in l:
        if r-1==0:
          if switch==False:
            e.append(r+1)
          else:
            switch=False
            e.append(r-1)
        else:
          if switch==False:
            e.append(r+1)
          else:
            e.append(r-1)

