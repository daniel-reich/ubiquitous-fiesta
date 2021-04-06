
def is_factorial(n):
  result = 1
  multiplier = 2
  while result < n:
    result = result * multiplier
    print(result)
    multiplier += 1
  print(result)
  if result == n:
    return True
  return False

