
def letters_only(txt):
  newstring = ''
  chars = [char for char in txt]
  for item in chars:
    if str(item).isalpha():
      newstring += item
    else:
      continue
  return newstring

