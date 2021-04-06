
def is_prime(n):
  return n > 1 and all(n % i for i in range(2, n))
​
def fat_prime(a, b):
  mx = a if a > b else b
  while not is_prime(mx):
    mx -= 1
  return mx

