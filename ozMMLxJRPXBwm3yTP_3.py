
def is_factorial(n):
  x,total = 1,1
  while total <= n:
    if total == n: return True
    x += 1
    total *= x
  return False

