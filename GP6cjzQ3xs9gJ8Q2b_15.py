
def is_polydivisible(n):
  num, d = n, 0
  while num: #find number of digits
    num //= 10
    d += 1
  while n:
    if n % d:
      return False
    n //= 10
    d -= 1
  return True

