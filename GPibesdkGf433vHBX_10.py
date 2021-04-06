
def is_prime(n):
  if n == 2: return True
  if not n % 2: return False
  for i in range(3, int(n ** 0.5) + 1, 2):
    if not n % i: return False
  return True
​
def goldbach_conjecture(n):
  for i in range(2, n):
    if is_prime(i) and is_prime(n - i):
      return [i, n - i]

