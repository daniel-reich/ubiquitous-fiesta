
def is_undulating(n):
  s = str(n)
  l = len(s)
  return l>2 and s == (s[:2]*l)[:l]

