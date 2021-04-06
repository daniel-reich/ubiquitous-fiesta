
def secret(txt):
  a = txt.split('.')
  b = ' '.join(a[1:])
  return "<{} class='{}'></{}>".format(a[0],b,a[0])

