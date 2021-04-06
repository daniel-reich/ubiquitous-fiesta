
def intersection(h1, h2):
  hi1, hi2 = {}, {}
  for key in set(h1.keys()).intersection(set(h2.keys())):
    hi1[key] = h1[key]
    hi2[key] = h2[key]
  return [hi1, hi2]

