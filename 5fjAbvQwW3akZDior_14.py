
def unrepeated(txt):
  unique = ''
  for el in txt:
    if el not in unique:
      unique += el
  return unique

