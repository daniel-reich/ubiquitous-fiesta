
def invert(s):
  if not s: return s
  return invert(s[1:]) + (s[0].upper() if s[0].islower() else s[0].lower())

