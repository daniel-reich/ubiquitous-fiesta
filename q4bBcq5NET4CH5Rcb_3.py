
def jay_and_bob(txt):
  d = {'half': 2, 'quarter':4, 'eighth': 8, 'sixteenth':16}
  
  return '{:.3g} grams'.format(round(28/d[txt],2))

