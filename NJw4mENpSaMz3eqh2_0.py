
def is_undulating(n):
  n = str(n)
  s = set(n[::2])
  t = set(n[1::2])
  return len(n) > 2 and len(s | t) == 2 and len(s) == len(t) == 1

