
def remove_special_characters(txt):
  new_txt = ''
  for char in txt:
    if char.isalnum() or char in {'-', '_', ' '}:
      new_txt += char
  return new_txt

