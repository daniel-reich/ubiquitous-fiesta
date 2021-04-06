
def map_letters(word):
  d = {}
  for i in range(len(word)):
    if word[i] not in d:
      d[word[i]] = [i]
    else:
      d.get(word[i]).append(i)
  return d

