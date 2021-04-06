
def simple_encoder(s):
  s = s.lower()
  for i in s:
    if s.count(i) == 1:
      s = s.replace(i, "[")
    else:
      s = s.replace(i, "]")
  return s

