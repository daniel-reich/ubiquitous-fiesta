
def is_prime(num):
  if num == 2 or num == 3:
    return True
  elif num < 2 or num % 2 == 0 or num % 3 == 0:
    return False
  for divisor in range(5, num // 2 + 1):
    if num % divisor == 0:
      return False
  return True
​
def prime_divisors(num):
  divisors_prime = []
  for divisor in range(2, num // 2 + 1):
    if num % divisor == 0 and is_prime(divisor):
      divisors_prime.append(divisor)  
  return divisors_prime

