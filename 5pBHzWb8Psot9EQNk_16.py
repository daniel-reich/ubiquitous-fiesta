
def simple_encoder(s):
  s = s.lower()
  res = ""
  for ch in s:
    if s.count(ch) == 1:
      res += '['
    else:
      res += ']'
  return res

