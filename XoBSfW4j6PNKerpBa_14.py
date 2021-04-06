
def complete_factorization(num):
  primes = [x for x in range(2, num + 1) if all(x % i for i in range(2, x))]
  factors = []
  while num != 1:
    for prime in primes:
      if num % prime:
        continue
      factors.append(prime)
      num //= prime
      break
  return sorted(factors)

