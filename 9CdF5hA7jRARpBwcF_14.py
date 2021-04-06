
def map_letters(word):
  dic = {}
  for i, c in enumerate(word):
    if c not in dic:
      dic[c] = [i]
    else:
      dic[c].append(i)
  return dic

