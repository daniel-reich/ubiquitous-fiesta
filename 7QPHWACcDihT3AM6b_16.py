
def can_find(bigrams, words):
  return all(i in str(words) for i in bigrams)

