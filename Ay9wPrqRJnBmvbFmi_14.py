
def halve_count(a, b):
  if a/2<=b:
    return 0
  return halve_count(a/2,b) + 1

