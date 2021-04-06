
def is_prime(n):
  if n > 1:
    for i in range(2, n):
      if n % i == 0:
        break
        return False
    else:
      return True
  
def prime_numbers(num):
  return len(list(filter(is_prime, range(1, num))))

