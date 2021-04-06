
def intersection(h1, h2):
  lst = []
  dct = {}
  dct2 = {}
  for i in h1:
    if i in h2:
      dct[i] = h1[i]
      dct2[i] = h2[i]
  return [dct, dct2]

