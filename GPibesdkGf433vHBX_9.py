
def is_prime(num):
  if num == 1:
    return False
  for i in range(2, num):
    if num % i == 0:
      return False
  return True
def goldbach_conjecture(n):
  if n % 2 != 0 or n <= 2:
    return []
  primes = [i for i in range(2, n) if is_prime(i)]
  reverse = primes[::-1]
  for num1 in primes:
    for num2 in reverse:
      if num1 + num2 == n:
        return [num1, num2]
      elif num1 + num2 < n:
        break

