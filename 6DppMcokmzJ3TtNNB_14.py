
def true_alphabetic(txt):
  spaces = []
  for a in range(len(txt)):
    if txt[a]==' ': spaces.append(a)
  new = sorted([a for a in txt if a!=' '])
  for s in spaces:
    new.insert(s,' ')
  return ''.join(new)

