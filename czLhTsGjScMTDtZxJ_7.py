
def is_prime(n):
  if n == 2: return True
  if not n % 2: return False
  for i in range(3, int(n ** 0.5) + 1, 2):
    if not n % i: return False
  return True
​
def primorial(n):
  ans, i, m = 1, 0, 2
  while i < n:
    if is_prime(m):
      ans *= m
      i += 1
    m += 1
  return ans

