
def prime_in_range(n1, n2):
  for x in range(n1, n2+1):
    if all(x % i != 0 for i in range(2, x)):
      return True
  return False

