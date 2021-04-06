
def license_plate(s, n):
  s = ''.join(c.upper() for c in s if c != '-')
  r = []
  while s:
    r.append(s[-n:])
    s = s[:-n]
  return '-'.join(reversed(r))

