
def is_prime(num):
  if num < 2:
    return False
  for i in range(2, num):
    if num % i == 0:
      return False
  return True
​
def prime_in_range(n1, n2):
  for j in range(n1, n2 + 1):
    if is_prime(j):
      return True
  return False

