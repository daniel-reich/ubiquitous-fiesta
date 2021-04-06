
def make_change(c):
  q = c // 25
  c %= 25
  d = c // 10
  c %= 10
  n = c // 5
  c %= 5
  p = c
  return {'q': q, 'd':d, 'n':n, 'p':p}

