
def equal(a, b, c):
  uniq = len(set([a, b, c]))
  if uniq == 1:
    return 3
  elif uniq == 2:
    return 2
  else:
    return 0

