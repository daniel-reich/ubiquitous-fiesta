
def all_prime(lst):
  for i in lst:
    for j in range(2,max(lst)):
      if i%j == 0 and i/j!=1:
        return False
      elif i == 1:
        return False
  return True

