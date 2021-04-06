
def halve_count(a, b, c = 0):
  a = a / 2
  if a <= b :
    return c
  return halve_count(a, b, c + 1)

