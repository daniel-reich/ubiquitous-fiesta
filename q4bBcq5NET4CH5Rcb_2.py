
def jay_and_bob(txt):
  d = {'half': 28 // 2, 'quarter': 28 // 4, 'eighth': 28 / 8, 'sixteenth': 28 / 16}
  return '{} grams'.format(round(d[txt], 2))

