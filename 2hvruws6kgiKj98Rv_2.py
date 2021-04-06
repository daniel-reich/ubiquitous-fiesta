
def to_scottish_screaming(txt):
  return ''.join([c if c not in 'aeiouAEIOU' else 'E' for c in txt]).upper()

