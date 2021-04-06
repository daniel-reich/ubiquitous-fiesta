
def prime_factorization(n):
  primes = [2, 3, 5, 7, 11, 13, 17, 19, 23]
  factors = []
  while n > 1:
    for p in primes:
      if not n % p:
        n //= p
        factors.append(p)
        break
  return factors

