
def can_find(bigrams, words):
  for x in bigrams:
    if x not in "".join(words):
      return False
  return True

