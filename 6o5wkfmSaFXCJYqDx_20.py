
def abcmath(a, b, c):
  if b == 0:
    return a % c == 0
  else:
    return abcmath(2*a, b-1, c)

