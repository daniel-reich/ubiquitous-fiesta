
def smallest(n):
  x=n
  n=n-1
  while(n>1):
    if(x%n!=0):
      i=1
      while((x*i)%n!=0):
        i+=1
      x=x*i
    n-=1
  return x

