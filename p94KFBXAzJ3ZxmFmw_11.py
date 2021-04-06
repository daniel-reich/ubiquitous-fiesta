
def ascii_capitalize(txt):
  return ''.join(i.lower() if ord(i)%2 else i.upper() for i in txt)

