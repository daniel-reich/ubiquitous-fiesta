
def non_repeats(n):
  i=0
  j=0
  s=0
  while(i<n):
    x=1
    j=0
    base=n-1
    z=0
    while(j<=i):
      x*=base
      j+=1
      z+=1
      if(z>=2):
        base-=1
    s+=x
    i+=1
  return s

