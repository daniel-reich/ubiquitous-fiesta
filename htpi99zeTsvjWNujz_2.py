
def halve_count(a, b):
  return 1 + halve_count(a/2, b) if a > b else -1

