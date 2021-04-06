
def to_scottish_screaming(txt):
  return ''.join(["E" if i.lower() in "aeiou" else i.upper() for i in txt])

