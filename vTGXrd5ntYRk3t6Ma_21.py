
def is_isogram(txt):
  uniques = ''
  for char in txt:
    if char.casefold() in uniques.casefold():
      continue
    else:
      uniques += char
  return  uniques == txt

