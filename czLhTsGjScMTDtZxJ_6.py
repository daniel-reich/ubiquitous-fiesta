
def is_prime(n):
  return sum(1 for x in range(2,n+1) if n%x==0 )==1
def primorial(n):
  cont,pn,prime=0,2,1
  while cont<n:
    if is_prime(pn):
      prime=prime*pn
      pn+=1
      cont+=1
    else: pn+=1
  return prime

