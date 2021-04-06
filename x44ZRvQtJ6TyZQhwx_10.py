
def is_pandigital(n):
  for x in range(10):
    if str(x) not in str(n):
      return False
  return True

