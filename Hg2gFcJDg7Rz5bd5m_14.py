
def intersection(h1, h2):
  tempDict1 = {}
  tempDict2 = {}
  for i in h1:
    if i in h2:
      tempDict1[i] = h1[i]
      tempDict2[i] = h2[i]
  return [tempDict1, tempDict2]

