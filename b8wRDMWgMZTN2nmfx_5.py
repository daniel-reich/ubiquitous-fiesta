
def equal(a, b, c):
  matches = 4 - len(set([a,b,c]))
  if matches == 1:
    matches = 0
  return matches

