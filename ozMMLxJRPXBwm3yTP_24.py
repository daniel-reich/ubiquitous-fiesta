
def is_factorial(n):
  for i in range (1, n):
    if n % i == 0:
      n /= i
      if n == 1:
        return True
    else:
      return False

