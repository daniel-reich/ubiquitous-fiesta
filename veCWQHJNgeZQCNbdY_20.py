
def root_digit(n):
  while n // 10 < 1:
    return n
  else:
    return root_digit(n // 10 + n % 10)

