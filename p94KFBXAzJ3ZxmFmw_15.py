
def ascii_capitalize(txt):
  new = [x.upper() if ord(x)%2==0 else x.lower() for x in txt]
  return ''.join(new)

