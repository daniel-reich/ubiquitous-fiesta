
def all_prime(lst):
  for x in lst:
    if x == 1:
      return False
    for i in range(2, x):
      if x % i == 0:
        return False
  return True

