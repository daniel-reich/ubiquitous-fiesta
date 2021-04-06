
def is_prime(n):
  if 2 < n < 4:
    return True
  for i in range(2, n):
    if n % i == 0:
      return False
  return True
​
def primes_below_num(n):
  primes_list = []
  for i in range(2, n + 1):
    if is_prime(i):
      primes_list.append(i)
  return primes_list

