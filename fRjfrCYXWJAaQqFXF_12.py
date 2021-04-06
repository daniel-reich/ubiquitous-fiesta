
def is_prime(num):
  for i in range(2, num):
    if num % i == 0:
      return False
  return True
​
​
def primorial(n):
  result = 1
  iterator = 2
  while n > 0:
    if is_prime(iterator):
      result *= iterator
      n -= 1
    iterator += 1
  return result

