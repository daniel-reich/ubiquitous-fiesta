
def ascii_capitalize(t):
  return ''.join(x.lower() if ord(x) % 2 else x.upper() for x in t)

