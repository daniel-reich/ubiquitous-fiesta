
def filter_primes(num):
  return [i for i in num if 2 in (i, 2**i%i)]

