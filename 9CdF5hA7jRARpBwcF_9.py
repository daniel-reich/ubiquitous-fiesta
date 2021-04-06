
def map_letters(word):
  d = {}
  for i, x  in enumerate(word):
    d[x] = d.get(x, []) + [i]
  return d

