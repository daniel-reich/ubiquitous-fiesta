
def simple_encoder(s):
  s = s.lower()
  return "".join(["[" if s.count(i) == 1 else "]" for i in s])

