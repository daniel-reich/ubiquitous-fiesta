
def to_scottish_screaming(txt):
  return ''.join(['E' if letter.upper() in ('AEIOU') else letter.upper() for letter in txt])

