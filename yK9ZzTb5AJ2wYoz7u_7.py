
def floyd(up_to = None, n_row = None):
  if up_to:
    i=1
    s=0
    while s<up_to:
      s+=i
      i+=1
    n=i-1
  else:
    n=n_row
  A=[x for x in range(1, n*(n+1)//2+1)]
  B=[]
  k=0
  t=0
  while t<n:
    t+=1
    k+=t
    B.append(A[k-t:k])
  return B

