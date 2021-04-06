
def trailing_zeros(n):
  res, i = 0, 5
  while i <= n:
    res += n // i
    i *= 5
  return res

