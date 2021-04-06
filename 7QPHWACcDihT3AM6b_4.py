
def can_find(bigrams, words):
  return all(i in ''.join(words) for i in bigrams)

