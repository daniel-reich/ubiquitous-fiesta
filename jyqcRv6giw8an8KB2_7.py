
def invert(s):
  return " ".join([w.swapcase()[::-1] for w in s.split()][::-1])

