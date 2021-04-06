
def wiggle_string(s):
  l = []
  for i in range(len(s)+1):
    l.append(' '*i + s)
  for i in range(len(s)-1,-1,-1):
    l.append(' '*i + s)
  return l

