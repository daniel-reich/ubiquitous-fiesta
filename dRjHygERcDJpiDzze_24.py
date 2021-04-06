
def lengthen(s1, s2):
  a, b = min(s1, s2, key=len), max(s1, s2, key=len)
  new = ''
  while len(new) < len(b):
    new += a
  return new[:len(b)]

