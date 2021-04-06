
def ascii_capitalize(txt):
  return ''.join([l.upper() if not ord(l) % 2 else l.lower() for l in txt])

