
def simple_encoder(s):
  return "".join(list("]" if s.lower().count(x)>=2 else "[" for x in s.lower()))

