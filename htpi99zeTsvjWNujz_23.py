
def halve_count(a, b):
  if a<=b:
    return -1
  return 1+halve_count(a/2,b)

