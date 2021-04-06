
def invert(s):
  return  invert(s[1:]) + s[0].swapcase() if s else ''

