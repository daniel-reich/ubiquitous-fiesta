
def all_prime(lst):
  return all(is_prime(i) for i in lst)
  
def is_prime(val):
  if val < 2:
    return False
  else:
    for i in range(2, val//2 + 1):
      if not val % i:
        return False
    return True

