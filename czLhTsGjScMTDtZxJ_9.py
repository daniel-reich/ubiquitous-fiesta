
def is_prime(n):
  if n == 1:
    return False
  for i in range(2, n):
    if n % i == 0:
      return False
  return True
def prod(lst):
  p = 1
  for num in lst:
    p *= num
  return p
def primorial(n):
  num = 2
  primes = []
  while len(primes) < n:
    if is_prime(num):
      primes.append(num)
    num += 1
  return prod(primes)

