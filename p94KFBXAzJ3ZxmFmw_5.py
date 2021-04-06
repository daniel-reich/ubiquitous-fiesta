
def ascii_capitalize(txt):
  return "".join([c.upper() if ord(c) % 2 == 0 else c.lower() for c in txt])

