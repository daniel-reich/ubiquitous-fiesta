
import math
def is_prime(number):
  if number % 2 == 0 and number > 2:
    return False
  for i in range(3, int(math.sqrt(number)) + 1, 2):
    if number % i == 0:
      return False
  return True
    
def prime_numbers(num):
  count_prime = 0
  while num > 1:
    if is_prime(num):
      count_prime += 1
    num -= 1
  return count_prime

