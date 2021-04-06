
def alternating_caps(txt):
  s = ''
  cnt = 0
  for c in txt:
    if c is not ' ':
      s += c.lower() if cnt % 2 else c.upper()
      cnt += 1
    else:
      s += c
  return s

