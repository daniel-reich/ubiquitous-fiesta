
def to_scottish_screaming(txt):
  return txt.lower().translate(str.maketrans('aeiou', 'eeeee')).upper()

