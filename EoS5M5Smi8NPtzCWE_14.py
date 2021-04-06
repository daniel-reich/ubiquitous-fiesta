
def secret(text):
  t = text.split('*')
  return ('<' + t[0] + '></' + t[0] + '>') * int(t[1])

