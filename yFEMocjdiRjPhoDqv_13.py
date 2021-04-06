
def prime_in_range(n1, n2):
  for i in range(n1, n2+1):
    if all(i%j != 0 for j in range(2, i)):
      return True
  return False

