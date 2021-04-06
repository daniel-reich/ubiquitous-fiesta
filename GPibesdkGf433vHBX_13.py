
def isprime(m):
  return [x for x in range(2,m+1) if m%x==0]==[m]
def goldbach_conjecture(n):
  a=[x for x in range(2,int(n/2)+1)]
  b=[x for x in range(n-2,int(n/2)-1,-1)]
  return [] if n%2 else [[v,n] for v,n in zip(a,b) if isprime(v) and isprime(n)][0]

