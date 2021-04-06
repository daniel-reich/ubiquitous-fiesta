
def root_digit(n):
  while n > 9:
    n = sum(map(int, str(n)))
  return n

