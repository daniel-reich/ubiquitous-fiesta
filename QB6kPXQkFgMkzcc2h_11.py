
def remove_abc(txt):
  a = txt.replace('a','')
  b = a.replace('b','')
  c = b.replace('c','')
  if c==txt:
    return None
  else:
    return c

