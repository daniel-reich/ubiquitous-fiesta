
def get_primes(n):
    numbers = set(range(n, 1, -1))
    primes = []
    while numbers:
        p = numbers.pop()
        primes.append(p)
        numbers.difference_update(set(range(p*2, n+1, p)))
    return primes
​
def prime_gaps(g, a, b):
  primes = get_primes(b)
  primes = [p for p in primes if p >= a]
  q = primes[0]
  for p in primes[1:]:
    if p - q  == g:
      return [q, p]
    q = p
  return None

