
def invert(s, res = ""):
  try:
    char = s[-1]
    s = s[:-1]
    if char.isupper():
      res += char.lower()
    else:
      res += char.upper()
    return invert(s,res)
  except:
    return res

