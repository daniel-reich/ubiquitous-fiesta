
def can_find(bigrams, words):
  return all([any([bg in w for w in words]) for bg in bigrams])

