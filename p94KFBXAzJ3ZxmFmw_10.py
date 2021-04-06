
def ascii_capitalize(txt):
  a =""
  for i in txt:
    if ord(i) % 2 == 0:
      b = i.upper()
      a+=b
    elif ord(i) % 2 != 0:
      c = i.lower()
      a+=c
  return a

