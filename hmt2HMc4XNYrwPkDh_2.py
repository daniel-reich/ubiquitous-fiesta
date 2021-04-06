
def opposite(s):
  return s.lower() if s.isupper() else s.upper()
def invert(s):
  if not s:
    return ""
  else:
    return opposite(s[-1]) + invert(s[:-1])

