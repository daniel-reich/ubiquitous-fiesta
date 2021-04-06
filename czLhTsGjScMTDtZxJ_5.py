
def is_prime(n):
  return n>1 and all(n%i for i in range(2,int(n**.5)+1))
def primorial(n):
  i=0
  c=0
  p=1
  while c<n:
    i+=1
    if is_prime(i):
      c+=1
      p*=i
  return p

