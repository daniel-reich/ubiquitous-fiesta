
def get_primes(ub):
  primes = [2]
  for c in range(3, ub + 1):
    if all(c % p != 0 for p in primes):
      primes.append(c)
  return primes
​
def power_count(n, f):
  c = 0
  while n % f == 0:
    c += 1
    n /= f
  return c
​
def express_factors(n):
  primes = get_primes(n)
  powers = [power_count(n, p) for p in primes]
  return ' x '.join('{}^{}'.format(p, f) if f > 1 else str(p) for p, f in zip(primes, powers) if f > 0)

