
def find_difference(a, b):
  a2 = 1
  b2 = 1
  for x in a:
    a2 *= x
  for x in b:
    b2 *=x
  return abs(a2 - b2)

