
def jay_and_bob(txt):
  grams = {
  "half":.5,
  "quarter":.25,
  "eighth":.125,
  "sixteenth": .0625
  }
  return '{} grams'.format(str(round(28*grams[txt],2)).rstrip('.0'))

