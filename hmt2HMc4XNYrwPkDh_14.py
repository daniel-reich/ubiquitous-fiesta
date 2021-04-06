
def invert(s):
  return '' if not s else s[-1].swapcase() + invert(s[:-1])

