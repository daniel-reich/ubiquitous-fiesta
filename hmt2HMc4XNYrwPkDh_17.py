
def invert(s):
  if len(s) == 1:
    return s.swapcase()
  else:
    return invert(s[1:]) + s[0].swapcase()

