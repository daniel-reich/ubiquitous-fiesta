
def sexy_primes(n,l):
  p=[x for x in range(l)if x>1and all(x%i for i in range(2,int(x**0.5+1)))]
  return([(x,x+6,x+12)for x in p if x+6in p and x+12in p],[(x,x+6)for x in p if x+6 in p])[n==2]

