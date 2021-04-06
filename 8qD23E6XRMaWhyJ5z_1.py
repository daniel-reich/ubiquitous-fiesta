
def happiness_number(s):
  c = 0
  for a, b in zip(s, s[1:]):
    if a + b in (':)', '(:'): c += 1
    if a + b in (':(', '):'): c -= 1
  return c

