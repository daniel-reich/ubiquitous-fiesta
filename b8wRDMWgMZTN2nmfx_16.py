
def equal(a, b, c):
  num = 0
  if a == b == c:
    num = 3
  elif a == b or a == c or b == c:
    num = 2
  return num

