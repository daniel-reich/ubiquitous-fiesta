
def ascii_capitalize(txt):
  return ''.join(c.lower() if ord(c) % 2 else c.upper() for c in txt)

