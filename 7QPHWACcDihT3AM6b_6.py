
def can_find(bigrams, words):
  for bi in bigrams:
    if bi not in ''.join(words):
      return False
  return True

