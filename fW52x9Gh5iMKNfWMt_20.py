
def recaman_index(n):
  r = [0]
  i = 0
  while r[i] != n:
    a = r[i] - len(r)
    if a > 0 and a not in r:
      r = r + [a]
    else:
      b = r[i] + len(r)
      r = r + [b]
    i += 1
  return i

