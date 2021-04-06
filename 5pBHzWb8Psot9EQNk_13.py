
def simple_encoder(s):
  s = s.lower()
  for a in s:
    if s.count(a)>1 and a!=']' and a!='[':
      s= s.replace(a, ']')
    elif s.count(a)==1 and a!=']' and a!='[':
      s=s.replace(a, '[')
  return s

