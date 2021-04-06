
def make_change(c):
  q, d, n, p = 0, 0, 0, 0
  while (c - 25) >= 0:
    q += 1
    c = c - 25
  while (c - 10) >= 0:
    d += 1
    c = c - 10
  while (c - 5) >= 0:
    n += 1
    c = c - 5
  p += c
  return dict([('q', q), ('d', d), ('n', n), ('p', p)])

