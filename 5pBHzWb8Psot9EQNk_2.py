
def simple_encoder(s):
  s = s.lower()
  t = ""
  for i in range(len(s)):
    if s.count(s[i]) == 1:
      t += "["
    else:
      t += "]"
  return t

