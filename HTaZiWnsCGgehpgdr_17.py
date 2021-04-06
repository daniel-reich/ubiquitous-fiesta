
def license_plate(s, n):
  new = ''
  s = s.upper()
  r = s.split("-")
  s = ""
  for i in r:
    s += i
  s = [e for e in s]
  r = len(s)
  for i in range(0, r % n):
    new += s[0]
    s.pop(0)
  if r % n > 0:
    new += "-"
  c = 0
  while (len(s) > 0):
    if c == n:
      c = 0
      new += "-"
    else:
      new += s[0]
      s.pop(0)
      c += 1
  return new

