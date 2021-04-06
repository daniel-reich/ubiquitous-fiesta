
def halve_count(a, b, count = -1):
  return halve_count(a/2, b, count+1) if a > b else count

