
def can_find(bigrams, words):
  return all(any(x in y for y in words) for x in bigrams)

