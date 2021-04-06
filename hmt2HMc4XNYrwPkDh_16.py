
def invert(s):
  if len(s) == 0: 
    return s 
  else:
    if s[0].isupper():
      return invert(s[1:]) + s[0].lower()
    else:
      return invert(s[1:]) + s[0].upper()

