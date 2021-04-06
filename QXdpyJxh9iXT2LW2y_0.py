
def semiprimes(n):
  primes = [k for k in range(n+1) if is_prime(k)]
  l = len(primes)
  semi_non_square = []
  for i in range(l):
    for j in range(i+1,l):
      if primes[i]*primes[j]<n:
        semi_non_square.append(primes[i]*primes[j])
  semi = semi_non_square + [p**2 for p in primes if p**2<n]
  return (sorted(semi), sorted(semi_non_square))
  
is_prime = lambda n: n>1 and all(n%i for i in range(2,1+int(n**.5)))

