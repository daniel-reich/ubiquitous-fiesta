
def halve_count(a, b):
  # recursive code here
  if a <= b:
    return -1
  else:
    return halve_count(a / 2, b) + 1

