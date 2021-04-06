
def find_the_difference(s, t):
  for c in s:
    t = t.replace(c, '', 1)
  return t

