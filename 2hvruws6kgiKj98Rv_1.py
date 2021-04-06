
def to_scottish_screaming(txt):
  return ''.join('E' if i in 'AEIOU' else i for i in txt.upper())

