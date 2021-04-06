
def can_find(bigrams, words):
  return all([any([x in i for i in words]) for x in bigrams])

