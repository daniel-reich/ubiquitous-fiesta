
def equal(a, b, c):
  txt = a,b
  x = sum(2 if c == i else 0 for i in txt)
  if x == 4:
    return x -1
  if x == 0:
    t = c,b
    return sum(2 if a == i else 0 for i in t)
  return x

