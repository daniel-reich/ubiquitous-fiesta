
def secret(txt):
  splitstr = txt.split('.')
  header = splitstr[0]
  return '<{} class=\'{}\'></{}>'.format(header,' '.join(splitstr[1:]),header)

