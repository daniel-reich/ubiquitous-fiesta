
def simple_check(a, b):
  a, b = sorted([a,b])
  c = 0
  while a != 0:
    c += not b%a
    a -= 1
    b -= 1
  return c

