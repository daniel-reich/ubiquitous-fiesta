
def combinations(k, n):
  j=n-k
  a=1
  b=1
  c=1
  while(n>1):
    a*=n
    n-=1
  while(k>1):
    b*=k
    k-=1
  while(j>1):
    c*=j
    j-=1
  return a//(b*c)

