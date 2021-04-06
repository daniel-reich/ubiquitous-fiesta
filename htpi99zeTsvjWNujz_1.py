
def halve_count(a, b, c=-1):
  if a <= b:
    return c
  else:
    return halve_count(a/2, b, c + 1)

