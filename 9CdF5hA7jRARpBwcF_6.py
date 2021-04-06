
def map_letters(word):
  d = {}
  for i,x in enumerate(word):
    if x not in d:  d[x] = [i]
    else: d[x].append(i)
  return d

