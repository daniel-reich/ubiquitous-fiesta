
def prime_factorize(num):
  primes = []
  x = 2
  while x <= num:
    if num % x == 0:
      num //= x
      primes.append(x)
    else:
      x += 1
  return primes

