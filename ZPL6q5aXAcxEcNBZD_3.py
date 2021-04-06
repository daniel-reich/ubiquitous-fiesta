
def funny_numbers(n, p):
  A=[int(x) for x in str(n)]
  s=sum([A[i]**(p+i) for i in range(len(A))])
  k,r=divmod(s,n)
  return k if r==0 else None

