
def to_scottish_screaming(txt):
  return (''.join(x if x.lower() not in 'aeiou' else 'e' for x in txt)).upper()

