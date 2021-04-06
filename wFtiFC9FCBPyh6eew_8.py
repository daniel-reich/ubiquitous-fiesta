
def partitions(n):
  
  cache = {}
  def par(n,m):
    if n==0:return 1
    t = 0
    if (n,m) in cache:return cache[(n,m)]
    for i in range(min(n,m),0,-1):
      t+=par(n-i,i)
    cache[(n,m)]=t
    return t
  return par(n,n)

