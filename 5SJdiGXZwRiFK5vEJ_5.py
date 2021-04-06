
def reverse_capitalize(txt):
  txt = txt[::-1]
  new_txt = ''
  for char in txt:
    char = char.upper()
    new_txt += char
  return new_txt

