
def simple_encoder(s):
  encode = ''
  s = s.lower()
  for elem in s:
    if s.count(elem) >=2:
      encode += ']'
    else:
      encode += '['
  return encode

