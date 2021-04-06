
def alternating_caps(txt):
  res, up = '', True
  for i in txt:
    if i.isalpha():
      res += i.upper() if up else i.lower()
      up = not up
    else: res += i
  return res

