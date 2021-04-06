
def cuban_prime(num, i=1):
  cuban = (i + 1) ** 3 - i ** 3
  if cuban > num:
    return '{} is not cuban prime'.format(num)
  if cuban == num and is_prime(num):
    return '{} is cuban prime'.format(num)
  return cuban_prime(num, i + 1)
  
def is_prime(n):
  return all(n % i for i in range(2, int(n ** 0.5) + 1))

