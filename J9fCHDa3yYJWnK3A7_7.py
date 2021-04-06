
def is_happy(n):
  if n == 1:
    return True
  elif n == 4:
    return False
  else:
    digits = [int(e) for e in str(n)]
    n = 0
    for digit in digits:
      n += digit ** 2
    return is_happy(n)

