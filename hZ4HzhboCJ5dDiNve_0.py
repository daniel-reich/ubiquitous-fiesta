
def special_reverse_string(txt):
  l = [i.lower() for i in txt[::-1] if not i.isspace()]
  for i, c in enumerate(list(txt)):
    if c.isupper():
      l[i] = l[i].upper()
    elif c.isspace():
      l.insert(i, ' ')
  return ''.join(l)

