
def to_scottish_screaming(txt):
  return ''.join('E' if x in 'AEIOU' else x for x in txt.upper())

