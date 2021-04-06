
def invert(s,res=''):
  if not s:
    return res
  return invert(s[:-1],res + s[-1].upper() if s[-1].islower() else res + s[-1].lower())

