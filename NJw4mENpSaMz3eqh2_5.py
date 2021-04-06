
def is_undulating(n):
  s = str(n)
  return len(s) > 2 and all(s.index(i) == idx % 2 for idx, i in enumerate(s))

