
def is_factorial(n):
  new = 2
  while True:
    n /= new
    if n == 1:
      return True
    if n < 1:
      return False
    new += 1

