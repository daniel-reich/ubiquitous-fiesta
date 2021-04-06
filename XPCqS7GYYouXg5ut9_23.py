
def simplify_sqrt(n):
  x = max(i for i in range(1,n//4+2) if n%(i*i)==0)
  return (x,n//(x*x))

