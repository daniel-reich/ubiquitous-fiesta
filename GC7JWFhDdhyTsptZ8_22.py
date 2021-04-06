
def sexy_primes(n, limit):
  it = 5
  lst = []
  while it < limit:
    if isPrime(it):
      check = True
      primes = [it]
      it2 = it + 6
      while check and len(primes) < n:
        if isPrime(it2) and it2 < limit:
          primes.append(it2)
          it2 += 6
        else:
          check = False
      if check:
        lst.append(tuple(primes))
    it += 1
  return lst
  
def isPrime(n):
  for i in range(2, n):
    if n%i == 0:
      return False
  return True

