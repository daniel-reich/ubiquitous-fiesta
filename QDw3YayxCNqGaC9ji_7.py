
def make_change(c):
  q = c // 25
  c %= 25
  d = c // 10
  c %= 10
  n = c // 5
  c %= 5
  p = c
  change = (q, d, n, p)
  return dict(zip('qdnp', change))

