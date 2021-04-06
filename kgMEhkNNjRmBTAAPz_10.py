
def remove_special_characters(txt):
  return txt.translate(dict.fromkeys(map(ord, r'`?^=|~*,&<>+[]{}()!@#$%.'), None))

