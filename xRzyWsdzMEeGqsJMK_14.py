
def maskify(txt):
  if txt[4:]:
    return '#' * (len(txt) - 4) + txt[-4:]
  return txt

