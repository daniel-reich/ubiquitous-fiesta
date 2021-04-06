
def filter_primes(num):
  primes = []
  for x in num:
    if x != 1:
      primes.append(x)
    for i in range(2,x):
      if x%i==0:
        primes.remove(x)
        break
  return primes

