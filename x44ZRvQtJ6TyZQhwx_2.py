
def is_pandigital(n):
  for i in range (10):
    if str(i) not in str(n):
      return False
  return True

