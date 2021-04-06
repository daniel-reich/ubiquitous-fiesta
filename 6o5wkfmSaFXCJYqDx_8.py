
def abcmath(a, b, c):
  i = 1
  while i <= b:
    a += a
    i += 1
  return a%c == 0

