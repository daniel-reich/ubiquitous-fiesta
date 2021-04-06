
def product_of_primes(n):
  p,c=2,1
  while n >=p*p:
    if n%p<1:c+=1;n/=p
    else:p+=1
  return c==2

