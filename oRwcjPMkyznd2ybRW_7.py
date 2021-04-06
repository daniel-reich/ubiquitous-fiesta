
def max_product(n,c=0):
  max=0;l=[]
  for i in range(1,n+1):
    p=1
    for j in str(i):
      p=p*int(j)
    if max<p:
      max=p
      a=i
      if c==1:
        l=[]
        c=0
    elif max==p:
      l.append(i)
      c=1
  l=[a]+l
  return l

