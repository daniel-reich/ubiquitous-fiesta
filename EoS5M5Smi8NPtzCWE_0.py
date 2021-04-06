
def secret(text):
  a = text.split("*")
  return "<{0}></{0}>".format(a[0])*int(a[-1])

