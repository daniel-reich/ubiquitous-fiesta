
def sum_digits(n):
  if n == 0:
    return 1
  res = 0
  while n != 0:
    n = n // 10
    res += 1
  return res

