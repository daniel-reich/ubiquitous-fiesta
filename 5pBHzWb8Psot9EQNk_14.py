
def simple_encoder(s):
  return ''.join('[' if s.lower().count(i) == 1 else ']' for i in s.lower())

