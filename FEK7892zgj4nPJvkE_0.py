
def prime_gaps(g,a,b):
  p=2
  for x in range(a,b+1):
    if all(x%i for i in range(2,int(x**0.5+1))):
      if x-p==g:return[p,x]
      else:p=x

