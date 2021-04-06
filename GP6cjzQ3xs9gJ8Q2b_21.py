
def is_polydivisible(n: int) -> bool:
  num_digits = len(str(n))
  while n >= 10:
    if n % num_digits != 0:
      return False
    n //= 10; num_digits -= 1
  return True

