
def secret(txt):
  cls, name = txt.split('.')[0], ' '.join(txt.split('.')[1:])
  return "<{0} class='{1}'></{0}>".format(cls, name)

