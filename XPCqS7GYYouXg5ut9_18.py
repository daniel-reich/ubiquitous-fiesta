
def simplify_sqrt(n):
  x,y = 1,n
  while perf_square(y)!=False:
    x,y = x*int(perf_square(y)**(1/2)),y//perf_square(y)
  return (x,y)
  
def perf_square(n):
  for i in range(4,n+1):
    if n%i==0 and i**(1/2)==int(i**(1/2)):
      return i
  return False

