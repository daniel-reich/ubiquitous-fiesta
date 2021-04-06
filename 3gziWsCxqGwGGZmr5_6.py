
def is_prime(num):
  for i in range(2, int(num ** 0.5 + 1)):
    if not num % i:
      return False
  return True
​
def fat_prime(*args):
  a, b = sorted(args, reverse=True)
  for j in range(a, b - 1, -1):
    if is_prime(j):
      return j

