
def is_powerful(n):
  primes = []
  for i in range(2,int(n**0.5)+1):
    for prime in primes:
      if i % prime == 0:
        break
    else:
      if n % i == 0 and n % (i*i) != 0:
        return False
      primes.append(i)
  return True

