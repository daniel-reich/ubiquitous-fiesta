
def invert(s):
  if len(s)==1:
    return s.upper() if s.islower() else s.lower()
  if s[-1].islower():
    return s[-1].upper()+invert(s[:-1])
  return s[-1].lower()+invert(s[:-1])

