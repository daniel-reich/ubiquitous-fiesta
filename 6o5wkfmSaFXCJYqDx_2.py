
def abcmath(a, b, c):
  for _ in range(b):
    a += a
  return bool(not(a%c))

