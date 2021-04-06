
def simple_encoder(s):
  s = s.lower()
  return ''.join(']' if s.count(x) > 1 else '[' for x in s)

