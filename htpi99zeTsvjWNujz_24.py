
def halve_count(a, b, c = -1):
  return halve_count(a, b * 2, c + 1) if a > b else c

