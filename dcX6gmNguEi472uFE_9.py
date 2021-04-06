
def double_factorial(n):
  if n <= 1:
    return 1
  else:
    return double_factorial(n-2) * n

