
def legendre(p, n):
  sum=0
  i=1
  while p**i<=n:
    sum+=n//(p**i)
    i+=1
  return sum

