
def ascii_capitalize(txt):
  return "".join((c.lower() if ord(c) & 1 else c.upper()) if c.isalpha() else c for c in txt)

