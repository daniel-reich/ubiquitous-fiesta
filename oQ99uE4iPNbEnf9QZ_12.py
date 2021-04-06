
def no_perms_digits(n):
  y = 1
  if n < 2:
    return 1
  else:
    for x in range(1, n + 1):
      y *= x
    return len(str(y))

