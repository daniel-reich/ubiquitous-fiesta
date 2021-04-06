
def is_prime(num):
  if num == 2:
    return True
  if num == 1: 
    return False
  for x in range(2, num):
    if not num % x:
      return False
  return True

