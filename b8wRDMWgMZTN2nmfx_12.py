
def equal(a, b, c):
  eq = 0
  if a == b and a == c and b == c:
    eq = 3
  elif a == b or a == c or b == c:
    eq = 2
  return eq

