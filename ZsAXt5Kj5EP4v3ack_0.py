
from re import sub
def secret(str):
  res = ''
  [a, b] = str.split('>')
  [c, d] = b.split('.')
  [e, f] = d.split('*')
  g = sub(r'[^a-z]', '', e)
  l = len(e) - len(g) - 1
  for i in range(1, int(f) + 1):
    res += "<{0} class='{1}{2}{3}'></{0}>".format(c, g, '0'*l, i)
  return "<{0}>{1}</{0}>".format(a, res)

