
def find_the_difference(s, t):
  s, t = sorted(s), sorted(t)
  for ch in s:
    t.remove(ch)
  return t[0]

