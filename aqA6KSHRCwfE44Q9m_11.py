
def normalize(txt):
  if all([c == ' ' or 'A' <= c <= 'Z' for c in txt]):
    return txt[0] + txt[1:].lower() + "!"
  return txt

