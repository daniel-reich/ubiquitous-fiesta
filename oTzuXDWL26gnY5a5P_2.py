
def is_prime(n):
  if n < 2:
    return False
  for i in range(2,n):
    if n % i == 0:
      return False
  return True
​
​
def prime_numbers(num):
  return sum([1 for x in range(num) if is_prime(x)])

