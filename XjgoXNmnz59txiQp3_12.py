
def split(n):
  x = [1,1,2,4]
  if n < 5:
    return x[n - 1]
  else:
    if n % 3 == 0:
      return 3 ** (n/3)
    if n % 3 == 1:
      return 3 ** (n // 3 - 1) * 4
    if n % 3 == 2:
      return 3 ** (n // 3) * 2

