
def deepest(lst):
  s=""
  c=1
  i=[]
  switch=True
  for t in lst:
    s=s+str(t)
  for r in s:
    if r=="[":
      c+=1
      switch=True
    elif r=="]":
      if switch==True:
        switch=False
        i.append(c)
        c-=1
      else:
        c-=1
  if len(i)==0:
    return 1
  else:
    return max(i)

