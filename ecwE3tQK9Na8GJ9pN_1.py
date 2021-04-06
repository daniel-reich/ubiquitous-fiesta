
def little_big(n):
  return 5 + n // 2 if n % 2 else 100 * 1 << n // 2 - 1

