
def find_the_difference(s, t):
  s = list(s)
  t = list(t)
  for i in s:
    t.remove(i)
  return t[0]

