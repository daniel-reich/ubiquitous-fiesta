
def is_factorial(n):
  a = 1
  for x in range(1, n):
    a *= x
    if a == n:
      return True
  return False

