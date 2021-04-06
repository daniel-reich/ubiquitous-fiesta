
def is_prime(n):
  if n == 2: return True
  if not n % 2: return False
  for i in range(3, int(n ** 0.5) + 1, 2):
    if not n % i: return False
  return True
​
​
def prime_gaps(g, a, b):
  n = None
  for i in range(a, b + 1):
    if is_prime(i):
      if n != None and i - n == g: return [n, i]
      n = i

