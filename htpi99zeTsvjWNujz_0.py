
def halve_count(a, b):
  if a / 2 <= b:
    return 0
  return 1 + halve_count(a/2,b)

