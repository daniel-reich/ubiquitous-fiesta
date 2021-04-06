
def to_scottish_screaming(txt):
  for char in txt:
    if char.lower() in 'aeiou':
      txt = txt.replace(char, 'e')
  return txt.upper()

