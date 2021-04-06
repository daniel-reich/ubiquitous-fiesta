
def partitions(n):
  c=1 if n<2 else 2
  x=[0 for i in range(n-1)]
  while x:
    sumx=sum(x)
    while n-sumx>=x[0]>0:
      c+=1
      x[0]+=1
      sumx+=1
    for i in range(n-1):
      x[i]+=1
      x=[x[i]+0 for j in range(i)]+x[i:]
      if n-sum(x)>=x[0]>0:break
    if all(x):break
  return c

