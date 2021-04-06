
def fat_prime(a, b):
  def is_prime(num):
    if num <= 1:
      return False
    for n in range(2, num):
      if num % n == 0:
        return False
    return True
  
  if b < a:
    a, b = b, a
  while is_prime(b) == False:
    b -= 1
  
  return b

