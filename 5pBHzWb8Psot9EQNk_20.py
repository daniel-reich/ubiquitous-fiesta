
def simple_encoder(s):
  return ''.join('[' if (s.lower()).count(x) == 1 else ']' for x in s.lower())

