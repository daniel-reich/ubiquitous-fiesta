
def all_prime(lst):
  for i in lst:
    if i == 1:
      return False
    for y in range(2, i-1):
      if i % y == 0:
        return False
  return True

