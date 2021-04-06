
def partitions(n):
  a=[0]*(n+1)
  a[0]=1
  for p in range(1,n+1):
      for idx, i in enumerate(range(p,n+1)):
        a[i]+=a[idx]
  return a[n]

