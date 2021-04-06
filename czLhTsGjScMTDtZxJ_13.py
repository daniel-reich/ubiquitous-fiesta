
is_prime = lambda x : all(x % i for i in range(2,x))
​
def primorial(n):
  primes = []
  x = 2
  while(n):
    if is_prime(x):
      primes.append(x)
      n -= 1
    x += 1  
  prod = primes[0]
  for i in range(1, len(primes)):
    prod *= primes[i]
  return prod

