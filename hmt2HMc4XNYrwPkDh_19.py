
def invert(s):
  if s == "": return ""
  return s[len(s)-1].swapcase() + invert(s[:len(s)-1])

