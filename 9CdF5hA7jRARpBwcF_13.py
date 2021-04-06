
def map_letters(word):
  mapped = {}
  for i in range(len(word)):
    if word[i] not in mapped:
      mapped[word[i]] = [i]
    else:
      mapped[word[i]].append(i)
  return mapped

