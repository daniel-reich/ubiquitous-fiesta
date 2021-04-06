
def bell(n):
  def fact(n):
    s=1
    for i in range(1,n+1):
      s=s*i
    return s
  
  def comb(n,k):
    return fact(n)//(fact(k)*fact(n-k))
    
  if n == 1 or n==0: return 1
  return sum(comb(n-1,k-1)*bell(n-k) for k in range(1,n+1))

