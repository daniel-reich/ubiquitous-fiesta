
def secret(text):
  a, b = text.split('*')
  return "<{0}></{0}>".format(a) * int(b)

