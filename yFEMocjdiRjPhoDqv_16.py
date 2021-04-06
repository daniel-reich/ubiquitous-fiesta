
def prime_in_range(n1, n2):
  def is_prime(number):
    if number == 2:
      return True
    if number < 2 or number % 2 == 0:
      return False
    for num in range(3, int(number**0.5) + 1, 2):
      if number % num == 0:
        return False
    return True
  
  for num in range(n1, n2 + 1):
    if is_prime(num):
      return True
  return False

