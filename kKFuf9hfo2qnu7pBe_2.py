
def is_prime(primes, num):
  lo = 0
  hi = len(primes)
  while hi-lo>1:
    h = (hi+lo)//2
    if num >= primes[h]:
      lo = h
    else:
      hi = h
  return 'yes' if primes[lo]==num else 'no'

