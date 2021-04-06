
def valid(txt):
  return len(txt) in [4, 6] and all(['0' <= c <= '9' for c in txt])

