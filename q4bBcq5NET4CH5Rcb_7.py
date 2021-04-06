
def jay_and_bob(txt):
    d = {'half': int(28 / 2), 'quarter': int(28 / 4),
         'eighth': 28 / 8, 'sixteenth': 28 / 16}
    return '{} grams'.format(d[txt])

