
def can_find(bigrams, words):
  words = ' '.join(words)
  return all(x in words for x in bigrams)

