
def map_letters(word):
  dict = {}
  for i,c in enumerate(word):
    if c not in dict:
      dict[c] = [i]
    else:
      dict[c].append(i)
  return dict

