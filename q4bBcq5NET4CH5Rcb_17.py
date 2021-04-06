
frac_dict = {
    'half': 2,
    'quarter': 4,
    'eighth': 8,
    'sixteenth': 16
  }
def jay_and_bob(txt):
  calc = 28 % frac_dict[txt]
  if not calc:
    return str(28 // frac_dict[txt]) + ' grams'
  else:
    return str(28 / frac_dict[txt]) + ' grams'

