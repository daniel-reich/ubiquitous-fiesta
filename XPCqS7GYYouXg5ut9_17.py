
def simplify_sqrt(n):
  m=max([x for x in range(1,int(n**0.5)+1) if n%(x**2)==0])
  return (m, n//(m**2))

