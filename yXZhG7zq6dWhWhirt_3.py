
def filter_primes(num):
  return [n for n in num if (all(n%i for i in range(2,n)) and n>1)]

