
def primorial(n, p=2):
  if n == 1:
    return p
  return p * primorial(n-1, next_prime(p))
        
def next_prime(n):
  while True:
    n += 1
    if all(n%i != 0 for i in range(2, n)):
      return n

