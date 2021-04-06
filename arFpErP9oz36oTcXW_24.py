
def secret(txt):
  t, *c = txt.split('.')
  return "<{0} class='{1}'></{0}>".format(t, ' '.join(c))

