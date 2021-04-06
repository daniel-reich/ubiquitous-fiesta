
def all_prime(lst):
  if 1 in lst:
    return False
  for i in lst:
    for j in range(2,i):
      if i%j == 0:
        return False
  return True

