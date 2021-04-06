
def ascii_capitalize(txt):
  return ''.join(s.lower() if ord(s) % 2 else s.upper() for s in txt)

