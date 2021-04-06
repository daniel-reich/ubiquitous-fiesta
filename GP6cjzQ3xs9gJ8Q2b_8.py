
def is_polydivisible(n):
  n = str(n)
  for i, digit in enumerate(n):
    num = n[:i+1]
    if int(num) % (i+1) != 0:
      return False
  return True

