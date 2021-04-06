
def prime_factorize(n):
  if not n-1:
    return []
  q = n
  primes = [x for x in range(n) if prime(x)]
  no = []
  i = 0
  while n>1 and i < len(primes):
    if not n%primes[i]:
      n //=primes[i]
      no.append(primes[i])
    if n%primes[i]:
      i+=1
  return no if no else [q]
    
  
def prime(n):
  return n>1 and not bool([x for x in range(2,int(n**.5)) if not n%x])

