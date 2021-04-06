
def josephus(people):
  t=[]
  for i in range(1,people+1):
    t.append(i)
  while len(t)>1:
    if len(t)%2==0:
      for i in range(1,len(t),2):
        t[i]=0
      t=sorted(list(set(t)))
      t.remove(t[0])
    else:
      t.remove(t[0])
      for i in range(0,len(t),2):
        t[i]=0
      t=sorted(list(set(t)))
      t.remove(t[0])
  return t[0]

