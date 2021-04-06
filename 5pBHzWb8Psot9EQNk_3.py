
def simple_encoder(s):
  return "".join(["[" if s.lower().count(c) == 1 else "]" for c in s.lower()])

