
def can_find(bigrams, words):
  return all(x in ' '.join(y for y in words) for x in bigrams)

