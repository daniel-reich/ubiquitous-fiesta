
def prime(num):
  if num == 2: return True
  if num in (0,1) or not num % 2: return True
  for n in range(2, num):
    if num % n == 0:
      return False
  return True
​
def is_prime(primes, num):
  primeiro = 0
  ultimo = len(primes) - 1
  while primeiro <= ultimo:
    metade = (ultimo + primeiro) // 2
    if primes[metade] < num:
      primeiro = metade + 1
    elif primes[metade] > num:
      ultimo = metade - 1
    else:
      return 'yes' if prime(num) else 'no'
  return 'no'

