
def secret(txt):
  txt, n = txt.split('*')
  return '<{0}></{0}>'.format(txt) * int(n)

