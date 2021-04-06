
def to_camel_case(t):
  if t == '': return ''
  j = [i for i in t if not i.isalpha()][0]
  t = t.split(j)
  s = t[0] + ''.join(i.title() for i in t[1:])
  return [s[0].upper()+s[1:], s][s[0].islower()]

