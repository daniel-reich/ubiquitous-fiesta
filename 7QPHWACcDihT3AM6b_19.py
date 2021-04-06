
def can_find(bigrams, words):
  return all(1 if i in "//".join(words) else 0 for i in bigrams)

