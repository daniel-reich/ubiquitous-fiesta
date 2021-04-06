
def abcmath(a, b, c):
  return a % c == 0 if b > 0 else abcmath(a + a, b - 1, c)

