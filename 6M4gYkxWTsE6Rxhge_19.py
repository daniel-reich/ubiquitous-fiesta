
def is_prime(num):
  if num > 1:
    for i in range(2,num):
      if (num % i) == 0:
        return False
    else:
      return True
  else:
    return False
def all_prime(lst):
  for i in lst:
    if not is_prime(i):
      return False
  return True

