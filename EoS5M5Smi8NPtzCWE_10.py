
def secret(text):
  n=int(text[-1])
  s=text[:-2]
  return '<{0}></{0}>'.format(s)*n

