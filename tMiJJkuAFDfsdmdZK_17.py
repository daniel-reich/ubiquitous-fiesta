
def to_snake_case(txt):
  return ''.join(x if x == x.lower() else '_'+x.lower() for x\
  in txt)
​
def to_camel_case(txt):
  s, toUp = "", False
  for x in txt:
    if x == "_":
      toUp = True
    elif toUp:
      s += x.upper()
      toUp = False
    else:
      s += x
  return s

