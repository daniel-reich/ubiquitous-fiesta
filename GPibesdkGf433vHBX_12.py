
def goldbach_conjecture(n):
  primes = get_primes(n)
  for p in primes:
    if n-p in primes:
      return [p, n-p]
  return []
​
def get_primes(N):
  return [n for n in range(2, N) if not any(not n%i for i in range(2, n))]

