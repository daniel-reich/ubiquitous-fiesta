
def is_prime(num):
  if num == 1:
    return False
  return len([x for x in range(2,num) if num % x == 0]) == 0

