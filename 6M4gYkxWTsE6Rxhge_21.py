
def all_prime(lst):
  for i in lst:
    if i == 1 or i == 0: return False
    for j in range(2, int(i**0.5)+1):
      if not i % j: return False
  return True

