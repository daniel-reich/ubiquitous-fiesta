
def filter_primes(N):
  return [n for n in N if 2 in [n, 2 ** n % n]]

