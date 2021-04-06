
def partitions(n):
  if n<1:return 1
  a=[0for i in range(n+1)]
  a[1],c,k=n,0,1
  while k!=0:
    x,y,k=a[k-1]+1,a[k]-1,k-1
    while x<=y:
      a[k],y,k=x,y-x,k+1
    a[k],c=x+y,c+1
  return c

