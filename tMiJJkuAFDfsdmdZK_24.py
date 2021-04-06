
def to_snake_case(txt):
  r = ""
  for a in txt:
    if a.isupper():
      r += "_"+a.lower()
    else:
      r += a
  return r
  
def to_camel_case(txt):
  r = ""
  u = False
  for a in txt:
    if a == "_":
      u = True
    elif u:
      r += a.upper()
      u = False
    else:
      r += a
  return r

