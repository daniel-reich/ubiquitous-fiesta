
def alternating_caps(txt):
  res = ''
  cap = True
  for ch in txt:
    res += ch.upper() if cap else ch.lower()
    if ch.isalpha():
      cap = not cap
  return res

