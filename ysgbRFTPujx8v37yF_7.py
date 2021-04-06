
def row_sum(n):
  if n%2:
    x=(n-1)//2
    return n*(1+4*(x*(x+1)//2))
  return (1+n**2)*(n//2)

