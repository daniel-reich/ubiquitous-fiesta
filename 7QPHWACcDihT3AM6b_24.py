
def can_find(bigrams, words):
  for bigram in bigrams:
    found = False
    for word in words:
      if bigram in word: found=True
    if not found: return False
  return True

