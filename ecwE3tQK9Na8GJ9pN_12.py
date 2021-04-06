
def little_big(n):
  if n % 2:
    return 5 + n // 2
  else:
    return 50 * (2 ** (n / 2))

