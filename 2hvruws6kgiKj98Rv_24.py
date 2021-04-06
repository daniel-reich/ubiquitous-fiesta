
def to_scottish_screaming(txt):
  return ''.join('e' if x.lower() in 'aeiou' else x for x in txt).upper()

