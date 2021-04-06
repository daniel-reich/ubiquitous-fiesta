
def ascii_capitalize(txt):
  return ''.join(i.upper() if ord(i) % 2 == 0 else i.lower() for i in txt)

