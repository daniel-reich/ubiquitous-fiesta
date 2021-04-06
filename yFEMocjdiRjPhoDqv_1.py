
def is_prime(n):
  return all(n % i for i in range(2, int(n**0.5) + 1))
​
​
def prime_in_range(n1, n2):
  for n in range(n1, n2 + 1):
    if is_prime(n):
      return True
  return False

