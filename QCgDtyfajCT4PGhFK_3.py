
def prime_factorization(number):
  primes = sieve(number + 1)
  factors = []
  for p in primes:
    while number % p == 0:
      number = number // p
      factors.append(p)
  return factors
​
def sieve(n):
  a = [True] * n
  a[0] = a[1] = False
  primes = []
  for i, is_prime in enumerate(a):
    if is_prime:
      primes.append(i)
      for j in range(i*i, n, i):
        a[j] = False
  return primes

