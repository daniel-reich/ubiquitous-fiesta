
def invert(s):
  return "" if s == "" else s[-1].swapcase() + invert(s[:-1])

