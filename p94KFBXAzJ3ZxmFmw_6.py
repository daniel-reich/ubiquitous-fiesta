
def ascii_capitalize(txt):
  newtxt = ""
  for c in txt:
    if ord(c) %2 == 0:
      newtxt+=c.upper()
    else:
      newtxt+=c.lower()
  return newtxt

