
def bed_time(*times):
  v=""
  b=""
  a=""
  e=""
  f=""
  l=[]
  switch=False
  for t in times:
    for c in t[0]:
      if switch==True:
        b=b+c
      elif c==":":
        v=int(v)
        switch=True
      elif switch==False:
        v=v+c
    b=int(b)
    switch=False
    for c in t[1]:
      if switch==True:
        e=e+c
      elif c==":":
        a=int(a)
        switch=True
      elif switch==False:
        a=a+c
    e=int(e)
    switch=False
    z=v-a
    w=b-e
    if w<0:
      z=z-1
      w=b+e
      w=abs(w)
    if w<10:
      w="0"+str(w)
    else:
      w=str(w)
    if z<0:
      z=24+z
    if z<10:
      z="0"+str(z)
    else:
      z=str(z)
    f=z+":"+w
    l.append(f)
    v=""
    b=""
    a=""
    e=""
    f=""
  return l

