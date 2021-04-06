
def extract_primes(num):
  def isprime(n):
    if n == 0 or n == 1:
      return False
    for x in range(2, n//2+1):
      if n % x == 0:
        return False
    return True
  primes = []
  for x in range(0, len(str(num))):
    if str(num)[x] == '0':
      continue
    for y in range(x, len(str(num))):
      if isprime(int(str(num)[x:y+1])):
        primes.append(int(str(num)[x:y+1]))
  primes.sort()
  return primes

