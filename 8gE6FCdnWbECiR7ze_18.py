
def smith_type(n):
  def prime_dec(n):
    l=[]
    for d in range(2,n+1):
      while n%d == 0:
        n//=d
        l+=[d]
    return l
  
  is_smith = lambda n: n%9 == sum(prime_dec(n))%9 and prime_dec(n)!=[n]
  
  if is_smith(n):
    if is_smith(n+1): return "Youngest Smith"
    if is_smith(n-1): return "Oldest Smith"
    return "Single Smith"
  if prime_dec(n)==[n]: return "Trivial Smith"
  return "Not a Smith"

